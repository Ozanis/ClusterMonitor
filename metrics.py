import psutil, subprocess, os

class VirtualMemory:

    def __init__(self):
        self.ram_obj = psutil.virtual_memory()
        self.swap_obj = psutil.swap_memory()

    def swap_stat(self):
        swap = { "total_swap": self.swap_obj,
                 "used_swap": self.swap_obj,
                 "%": self.swap_obj.percent
        }
        return swap

    def ram_stat(self):
        virtual_mem = {
            "total_ram": self.ram_obj.total,
            "used_ram": self.ram_obj.used,
            "%": self.ram_obj.percent
        }
        return virtual_mem

    def __repr__(self):
        return str(self.swap_stat())+str(self.swap_stat())

class Processor:

    def __init__(self):
        self.low_level_info = psutil.cpu_stats()
        self.cpu_stat = {
            "count_physical": psutil.cpu_count(logical=False),
            "count_logical": psutil.cpu_count(logical=True),
            "per_core_usage": psutil.cpu_percent(interval=1, percpu=True)
            "cpu_freq": psutil.cpu_freq(percpu=True),
            "cpu_using": psutil.cpu_times_percent(interval=None, percpu=False)
        }

    def __repr__(self):
        return str(self.low_level_info)+str(self.cpu_stat)


class Prcss:

    def __init__(self):

    def list(self):

    def critical(self):

    def critical_load(self):

class Network:

    def __init__(self):

    def __repr__(self):


class Outp:

    def __init__(self):

    def __repr__(self):__: