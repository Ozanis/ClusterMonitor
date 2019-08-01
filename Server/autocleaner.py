from threading import Thread, ThreadError
from psutil import NoSuchProcess, pid_exists, Process
from time import sleep
from os import stat, listdir, remove
#import ctypes


class Cleaner:

    def __init__(self, directory):
        try:
            self.pid = Process().ppid()
            print(self.pid)
        except NoSuchProcess:
            print("Error of autocleaner starting: no parent process")
            exit(1)
        self.work_path = directory

    def conns(self):
        if stat(self.work_path).st_size >= 3145728:
            pids = Process.threads(self.pid)
            for i in pids:
                if i == Process().pid:
                    del pids[i]
            print(pids)
            if pids is not []:
                return pids
        return None

    def flush(self):
        for i in listdir(self.work_path):
            remove(i)

    @staticmethod
    def cont(*args):
        for i in args:
            if pid_exists(i):
                Process.resume(i)
            else:
                del i

    @staticmethod
    def stop(*args):
        if args is not [] and None not in args:
            for i in args:
                if pid_exists(i):
                    Process.suspend(i)
                else:
                    del i

    def handle(self, *args):
        if args is None:
            Process.suspend(self.pid)
            self.flush()
            self.cont()
            Process.resume(self.pid)
        else:
            self.stop(*args)
            self.flush()
            self.cont()

    def clean(self):
        print("Autoclean start")
        while pid_exists(self.pid):
            pids = self.conns()
            print(pids)
            if pids is not None:
                print(1)
                self.handle(pids)
            sleep(1)


def enable(work_direct):
    autoclean = Cleaner(work_direct)
    try:
        Thread(target=autoclean.clean(), args="").start()
        print("Autoclean enable")
    except ThreadError:
        print("Failed to fork autocleaner")
        exit(1)
