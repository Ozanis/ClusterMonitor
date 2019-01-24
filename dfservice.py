import telemetry_client, logging, threading
from sys import exit
from gzip import compress
from psutil import Process
from metrics import Telemetry, Prcss
from subprocess import Popen
from Tools import internet, boot_disp
from time import time, sleep
from os import getcwd, remove


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


def log():
    temp_log()
    if add_log():
        server(addr="35.247.6.149")
        sleep(5)
    else:
        pass


def critical_monitor():
    monitor = Prcss()
    logging.basicConfig(filename=str(getcwd()) + "/log/critical.log", level=logging.INFO)
    _val = ""
    while True:
        critical_pids = monitor.critical_prcss()
        if critical_pids is None:
            pass
        elif critical_pids == _val:
            pass
        else:
            critical_names = [Process(i).name() for i in critical_pids]
            critical_processes = "Critical processes: " + str(critical_names)
            del critical_names
            Popen(['notify-send', "Warning:", critical_processes])
            logging.info(critical_processes)
            del critical_processes
            _val = str(critical_pids)
            del critical_pids
            try:
                threading.Thread(target=log, args="").start()
            except threading.ThreadError:
                logging.error("Can`t  start critical monitoring")
                Popen(['notify-send', "Warning: Unable to start monitoring"])
                exit(1)
        sleep(5)


if __name__ == "__main__":
    sleep(5)
    boot_disp()
    log()
    critical_monitor()
    exit(0)
