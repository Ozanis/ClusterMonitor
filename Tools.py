import logging, os, subprocess, metrics, psutil, re
from time import sleep, time

"""
Self Service`s log and self debug tools:
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
        logging.basicConfig(filename=str(os.getcwd()) + "/log/self_log.log")
        logging.info("---Get executional data---")
        exc = f(*args, **kwargs)
        logging.info("Used CPU: %s" % psutil.cpu_percent(p))
        logging.info("Execution time: " + str((time() - t)))
        logging.info("---Get executional data---")
        return exc
    return test


def internet():
    try:
        subprocess.check_call(["ping", "-c 1", "www.google.ru"])
        return True
    except subprocess.CalledProcessError:
        logging.warning("No internet. Extra stopping")
        subprocess.Popen(['notify-send', "Warning: check your internet connection or possibly google host ureachable :)"])
        sleep(5)
        return False


def critical_monitor():
    monitor = metrics.Prcss()
    logging.basicConfig(filename=str(os.getcwd()) + "/log/critical.log", level=logging.INFO)
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
            del critical_names
            subprocess.Popen(['notify-send', "Warning:", critical_processes])
            logging.info(critical_processes)
            _val = str(critical_pids)
        sleep(6)


def boot_disp():
    boot = None
    try:
        boot = subprocess.Popen(["systemd-analyze"], shell=False)
    except subprocess.SubprocessError:
        subprocess.Popen(['notify-send', "Unable to read boot time"])
    t=""
    for i in str(boot):
        if i == "=":
            i += 2
            t=i
        if t != "":
            t += i
    subprocess.Popen(['notify-send', "Boot time:", t])


boot_disp()
#def temp():
 #   t = metrics.Hardware().temp
  #  for i in t:
