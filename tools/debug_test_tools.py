import logging, os
from time import time as time
import psutil
"""
Self Service`s logs and self debug tools:
Time of self execution
CPU of self execution
RAM of self execution
"""


def timer(f):
    def test(*args, **kwargs):
        t = time()
        exc = f(*args, **kwargs)
        print("Execution time: %s" % (time()-t))
        return exc
    return test


def check_cpu(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        print("Used CPU: %s" % psutil.cpu_percent())
        return exc
    return test


def check_ram(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        print("Used RAM: %s" % psutil.virtual_memory())
        return exc
    return test


def logg(f):
    def test(*args, **kwargs):
        p = psutil.Process.pid
        t = time()
        logging.basicConfig(filename=str(os.getcwd()) + "/logs/self_log.log")
        logging.info("---Get executional data---")
        exc = f(*args, **kwargs)
        logging.info("Used CPU: %s" % psutil.cpu_percent(p))
        logging.info("Execution time: " + str((time() - t)))
        logging.info("---Get executional data---")
        return exc
    return test

