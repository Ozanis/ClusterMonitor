import telemetry_client, logging, threading
from sys import exit
from gzip import compress
from metrics import Telemetry
from time import time, sleep
from os import getcwd, remove
from subprocess import Popen
from Tools import internet, critical_monitor, boot_disp

"""Main script"""


def add_log():
    _buf = ""
    path = str(getcwd()) + "/log/"
    try:
        f = open(path + "temp.log")
        _buf = f.read()
        f.close()
    except IOError:
        Popen(['notify-send', "Error: Unable read temp log"])
        return False
    try:
        path += "telemetry.log"
        f = open(path, "a")
        f.write(_buf)
        f.close()
        del _buf
    except IOError:
        Popen(['notify-send', "Error: Unable to add new log"])
        return False
    else:
        return True


def temp_log():
    telemetry = Telemetry()
    log_time = time()
    try:
        telemetry.to_do_logs()
    except RuntimeError:
        logging.info("---FINISHED WITH ERRORS---")
        Popen(['notify-send', "Runtime service`s error"])
    logging.info("Execution time: %s" % (str((time() - log_time))))


def cmprss(val):
    buf = None
    try:
        buf = compress(val, compresslevel=9)
    except TypeError:
        logging.error("Error of compressing")
        Popen(['notify-send', "Compress error"])
        exit(1)
    else:
        return buf


def server(addr):
    while not internet(host=addr):
        sleep(5)
    chnl = telemetry_client.SockSsl()
    path = str(getcwd()) + "/log/temp.log"
    try:
        with open(path, "rb") as _f:
            _buf = _f.read()
            data = compress(_buf)
            chnl.con(host=addr)
            chnl.send(data)
    except IOError:
        Popen(['notify-send', "Error: corrupted temp log file"])
        return False
    try:
        remove(path)
    except FileNotFoundError:
        return False
    else:
        return True


if __name__ == "__main__":
    sleep(5)
    boot_disp()
    temp_log()
    if add_log():
        server(addr="35.247.6.149")
        sleep(5)
    else:
        pass
    Tmonitor = threading.Thread(target=critical_monitor(), args="")
    Tmonitor.start()

    exit(0)
