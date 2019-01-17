import subprocess, logging, time, metrics, psutil


def internet():
    try:
        subprocess.check_call(["ping", "-c 1", "www.google.ru"])
        return True
    except subprocess.CalledProcessError:
        logging.warning("No internet. Extra stopping")
        subprocess.Popen(['notify-send', "Warning: check your internet connection or possibly google host ureachable :)"])
        time.sleep(5)
        return False


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
