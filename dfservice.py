import sys, telemetry_server, controller, metrics, threading, logging, debug_test_tools, os, time, subprocess

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

def log():
    telemetry = metrics.Telemetry()
    log_time = time.time()
    # logging.basicConfig(filename=str(os.getcwd()) + "/logs/self_log.log")
    try:
        telemetry.to_do_logs()
    except RuntimeError:
        logging.info("---FINISHED WITH ERRORS---")
        subprocess.Popen(['notify-send', "Runtime service`s error"])
    logging.info("Execution time: %s" % (str((time.time() - log_time))))

def server():
    server = telemetry_server.SockSsl()
    server.set()
    server.send()

if __name__=="__main__":
    log()
    server()

    sys.exit(0)
