import sys, telemetry_server, controller, metrics, threading, logging, debug_test_tools, os, time, subprocess, psutil

"""Main script"""

"""
class Service:
    def __init__(self):
        self.telemetry = metrics.Telemetry()
        self.log_time = time.time()

    def log(self):
        #logging.basicConfig(filename=str(os.getcwd()) + "/logs/self_log.log")
        try:
            self.telemetry.to_do_logs()
        except RuntimeError:
            logging.info("---FINISHED WITH ERRORS---")
            subprocess.Popen(['notify-send', "Runtime service`s error"])
        logging.info("Execution time: %s" % (str((time.time() - self.log_time))))

    def __del__(self):
        del self.telemetry
        del self.log_time
"""

def add_log():
    try:
        with open(path) as f:
            _buf = f.read()
            _log = str(os.getcwd()) + "/log/telemetry_log.log"
            try:
                with open(_log, "a") as _f:
                    _f.write(_buf)
            except IOError:
                subprocess.Popen(['notify-send', "Error: Unable to add new log"])
                return False
    except IOError:
        subprocess.Popen(['notify-send', "Error: Unable read temp log"])
        return False
    return True

def log():
    telemetry = metrics.Telemetry()
    log_time = time.time()
    try:
        telemetry.to_do_logs()
    except RuntimeError:
        logging.info("---FINISHED WITH ERRORS---")
        subprocess.Popen(['notify-send', "Runtime service`s error"])
    logging.info("Execution time: %s" % (str((time.time() - log_time))))


def critical_monitor():
    monitor = metrics.Prcss()
    _val = ""
    while True:
        critical_pids = monitor.critical_prcss()
        if critical_pids is None:
            break
        elif critical_pids == _val:
            break
        else:
            critical_names = [psutil.Process(i).name() for i in critical_pids]
            critical_processes = "Critical processes: " + str(critical_names)
            subprocess.Popen(['notify-send', critical_processes])
            _val = critical_pids
        time.sleep(6)


def server():
    try:
        subprocess.check_call(["ping", "-c 1", "www.google.ru"])
    except subprocess.CalledProcessError:
        logging.warning("No internet. Extra stopping")
        subprocess.Popen(['notify-send', "Warning: check your internet connection or possibly google host ureachable :)"])
        return False
    con = telemetry_server.SockSsl()
    con.set()
    try:
        with open(path, "rb") as _buf:
            con.send(_buf)
            return True
    except IOError:
        subprocess.Popen(['notify-send', "Error: corrupted temp log file"])
        return False


if __name__ == "__main__":
    path = str(os.getcwd()) + "/logs/temp.log"
    log()
    if server():
        if add_log():
            os.remove(path)
    _Tmonitor = threading.Thread(target=critical_monitor(), args="")
    _Tmonitor.start()

    sys.exit(0)
