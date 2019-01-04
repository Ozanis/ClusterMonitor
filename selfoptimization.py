import time

"""Time of self execution"""


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        exc = f(*args, **kwargs)
        print("Execution time", time.time()-t)
        return exc
    return tmp
