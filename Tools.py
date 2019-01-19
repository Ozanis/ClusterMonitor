import logging
from os import getcwd
from subprocess import check_call, CalledProcessError, Popen, SubprocessError, getoutput
from metrics import Prcss
from psutil import cpu_percent, virtual_memory, Process
from time import sleep, time


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
        print("Used CPU: %s" % cpu_percent())
        return exc
    return test


def check_ram(f):
    def test(*args, **kwargs):
        exc = f(*args, **kwargs)
        print("Used RAM: %s" % virtual_memory())
        return exc
    return test


def logg(f):
    def test(*args, **kwargs):
        p = Process.pid
        t = time()
        logging.basicConfig(filename=str(getcwd()) + "/log/self_log.log")
        logging.info("---Get executional data---")
        exc = f(*args, **kwargs)
        logging.info("Used CPU: %s" % cpu_percent(p))
        logging.info("Execution time: " + str((time() - t)))
        logging.info("---Get executional data---")
        return exc
    return test


def internet(host):
    try:
        check_call(["ping", "-c 1", "www.google.ru"])
    except CalledProcessError:
        logging.warning("No internet. Extra stopping")
        Popen(['notify-send', "Warning: check your internet connection or possibly google host ureachable :)"])
        sleep(5)
        return False
    try:
        check_call(["ping", "-c 1", host])
    except CalledProcessError:
        logging.warning("No connection with the server")
        Popen(
            ['notify-send', "Warning: Connection with the server is missing"])
        return False
    return True


def critical_monitor():
    monitor = Prcss()
    logging.basicConfig(filename=str(getcwd()) + "/log/critical.log", level=logging.INFO)
    _val = ""
    while True:
        critical_pids = monitor.critical_prcss()
        if critical_pids is None:
            break
        elif critical_pids == _val:
            break
        else:
            critical_names = [Process(i).name() for i in critical_pids]
            critical_processes = "Critical processes: " + str(critical_names)
            del critical_names
            Popen(['notify-send', "Warning:", critical_processes])
            logging.info(critical_processes)
            _val = str(critical_pids)
        sleep(6)


def boot_disp():
    boot = None
    try:
        boot = str(getoutput("systemd-analyze"))
    except SubprocessError:
        Popen(['notify-send', "Unable to read boot time"])
    t = ""
    for i in boot:
        if i == "=":
            t = ":"
            continue
        if t != "":
            t += i
            if "s" in t:
                break
    Popen(['notify-send', "Boot time%s" % t])

