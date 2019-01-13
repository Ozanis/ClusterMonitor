import subprocess, logging, time


def internet():
    try:
        subprocess.check_call(["ping", "-c 1", "www.google.ru"])
        return True
    except subprocess.CalledProcessError:
        logging.warning("No internet. Extra stopping")
        subprocess.Popen(['notify-send', "Warning: check your internet connection or possibly google host ureachable :)"])
        time.sleep(5)
        return False

