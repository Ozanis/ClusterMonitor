import sys, telemetry_server, controller, metrics, threading, logging, debug_test_tools, os, time, subprocess

"""Main script"""


class Service:
    def __init__(self):
        self.telemetry = metrics.Telemetry()
        self.log_time = time.time()
        logging.basicConfig(filename=str(os.getcwd()) + "/logs/self_log.log")

    def log(self):
        try:
            self.telemetry.to_do_logs()
        except RuntimeError:
            logging.info("---FINISHED WITH ERRORS---")
        logging.info("Execution time: %s" % (str((time.time() - self.log_time))))
        subprocess.Popen(['notify-send', "Error: Unable to write telemetry data"])

    def __repr__(self):
        del self.telemetry
        del self.log_time


