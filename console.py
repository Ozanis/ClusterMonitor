import os, signal, sys, subprocess


class Console:

    def __init__(self):
        self.com_list = {
            "--stop",
            "--start",
            "--dsbl autostop",
            "--restore",
            "--clear logs",
            "--support",
            "--DF"}

    def stop(self):
        return

    def start(self):
        return

    def dsbl(self):
        return

    def restore(self):
        return

    def clear(self):
        return

    def support(self):
        return

    def DF(self):
        return


    def classcomand(self, f):
        def choise(*args, **kwargs):
            c = f(*args, **kwargs)
            if "--stop" in inp:
                self.stop()
            elif "--start" in inp:
                self.start()
            elif "--dsbl autostop" in inp:
                self.dsbl()
            elif "--restore" in inp:
                self.restore()
            elif "--stop" in inp:
                self.clear()
            elif "--stop" in inp:
                self.support()
            elif "--stop" in inp:
                self.DF()
            else:
                print("wrong")
            return c
        return choise

    @classcomand
    def inp_cmd(self, inp):
        cmnd = (i for i in self.com_list if i in self.com_list)


#class Daemon:
