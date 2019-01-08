import logging, os
from time import time as time
from psutil import cpu_percent as cpu
from psutil import virtual_memory as ram

"""
Self Service`s logs and self debug tools:
Time of self execution
CPU of self execution
RAM of self execution
"""


class Test:

    def __init__(self):
        self.logs = logging.basicConfig(filename=str(os.getcwd()) +"logs/self_log.log")
        logging.info("---Get executional data---")


def timer(f):
    def test(*args, **kwargs):
        t = time()
        exc = f(*args, **kwargs)
        logging.info("Execution time: %s" % (time()-t))
        return exc
    return test


def check_cpu(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        logging.info("Used CPU: %s" % cpu())
        return exc
    return test


def check_ram(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        logging.info("Used RAM: %s" % ram())
        return exc
    return test
