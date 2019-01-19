import sys, telemetry_client, metrics, logging, os, time, subprocess, Tools, threading

"""Main script"""


def add_log():
    _buf = ""
    path = str(os.getcwd()) + "/log/"
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


def server():
    while not Tools.internet():
        time.sleep(5)
    chnl = telemetry_client.SockSsl()
    path = str(os.getcwd()) + "/log/temp.log"
    try:
        with open(path, "rb") as _f:
            _buf = _f.read()
            chnl.con(_buf)
    except IOError:
        subprocess.Popen(['notify-send', "Error: corrupted temp log file"])
        return False
    try:
        os.remove(path)
    except FileNotFoundError:
        return False
    else:
        return True


if __name__ == "__main__":
    time.sleep(5)
    Tools.boot_disp()
    temp_log()
    if add_log():
        server()
        time.sleep(6)
    else:
        pass
    Tmonitor = threading.Thread(target=Tools.critical_monitor(), args="")
    Tmonitor.start()

    sys.exit(0)
