import subprocess, os, sys, psutil

"""diagnosing and autostopping possibly dangerous processes and own wrong threads"""


class SelfOwerload():

    def __init__(self):
        self.proc = psutil.Process()
        self.pid = self.proc.pid

    def self_monitor(self):
        while True:
            if self.proc.cpu_percent(interval=3) >= 2:
                self.proc.suspend(self.pid)
            if self.proc.memory_percent() >= 1:
                self.proc.suspend(self.pid)

    def conrol(self):
        for subproc in self.proc.children():
            if self.proc.cpu_percent(interval=3) >= 2:
                self.proc.terminate(subproc)
            if self.proc.memory_percent() >= 1:
                self.proc.terminate(subproc)


