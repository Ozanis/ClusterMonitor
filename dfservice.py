import sys, telemetry_server, metrics, logging, os, time, subprocess, Tools, threading
from console import console

"""Main script"""


def add_log(path):
    path += "/log/"
    _buf = ""
    try:
        f = open(path + "temp.log")
        _buf = f.read()
        f.close()
    except IOError:
        subprocess.Popen(['notify-send', "Error: Unable read temp log"])
        return False
    try:
        path += "telemetry.log"
        f = open(path, "a")
        f.write(_buf)
        f.close()
        del _buf
    except IOError:
        subprocess.Popen(['notify-send', "Error: Unable to add new log"])
        return False
    else:
        os.remove(path)
    return True


def temp_log():
    telemetry = metrics.Telemetry()
    log_time = time.time()
    try:
        telemetry.to_do_logs()
    except RuntimeError:
        logging.info("---FINISHED WITH ERRORS---")
        subprocess.Popen(['notify-send', "Runtime service`s error"])
    logging.info("Execution time: %s" % (str((time.time() - log_time))))


def server(path):
    while not Tools.internet():
        time.sleep(5)
    con = telemetry_server.SockSsl()
    try:
        with open(path + "temp.log", "rb") as _buf:
            con.send(_buf)
            return True
    except IOError:
        subprocess.Popen(['notify-send', "Error: corrupted temp log file"])
        return False


if __name__ == "__main__":
    time.sleep(5)
    Tools.boot_disp()
    path = str(os.getcwd()) + "/log/"
    temp_log()
    if add_log(path):
        server(path)
    else:
        pass
    time.sleep(1)

    Tmonitor = threading.Thread(target=Tools.critical_monitor(), args="")
    Tmonitor.start()

    sys.exit(0)
