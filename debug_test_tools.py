from time import time as time
from psutil import cpu_percent as cpu
from psutil import virtual_memory as ram
"""Time of self execution"""


def timer(f):
    def test(*args, **kwargs):
        t = time()
        exc = f(*args, **kwargs)
        print("Execution time", time()-t)
        return exc
    return test


"""CPU of self execution"""


def check_cpu(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        print("Using CPU", cpu)
        return exc
    return test


"""RAM of self execution"""


def check_ram(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        print("Using RAM", ram())
        return exc
    return test

"""Self Service`s logs"""