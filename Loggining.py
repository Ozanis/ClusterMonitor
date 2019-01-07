import logging, datetime

log_server =

"""Telemetry logs"""
def log_server_con(f):
    logging.basicConfig(level=logging.info)
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)

        return exc
    return test


"""System logs"""


"""Pushing"""