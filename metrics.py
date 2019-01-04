import psutil, os

"""General RAM and SWAP using"""

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

    def __del__(self):
        del self.ram_obj
        del self.swap_obj


"""Monitoring sensors"""

class Hardware:

    def __init__(self):
        self.boot = psutil.boot_time()

    def __repr__(self):
        hrdw = {
            "power": psutil.sensors_battery(),
            "fans": psutil.sensors_fans(),
            "temp": psutil.sensors_temperatures(fahrenheit=False)
        }
        return str(hrdw)

    def __del__(self):
        del self.boot


"""CPU working state"""

class Processor:

    def __init__(self):
        self.low_level_info = psutil.cpu_stats()
        self.cpu_stat = {
            "count_physical": psutil.cpu_count(logical=False),
            "count_logical": psutil.cpu_count(logical=True),
            "per_core_usage": psutil.cpu_percent(interval=1, percpu=True),
            "cpu_freq": psutil.cpu_freq(percpu=True),
            "cpu_using": psutil.cpu_times_percent(interval=None, percpu=False)
        }

    def __repr__(self):
        return str(self.low_level_info)+str(self.cpu_stat)

    def __del__(self):
        del self.low_level_info
        del self.cpu_stat


"""Monitoring RAM and CPU owerload """

class Prcss:

    def __init__(self):
        self.handler = psutil.Process()
        self.dir = str(os.getcwd())

    def proc_log(self):
        proc = psutil.process_iter(attrs=["pid", "name"])
        with open(self.dir + "/logs/logs.txt", "w") as _f:
            _f.write(proc.info)

    def critical_prcss(self):
        c_load=psutil.cpu_percent()
        m_load=psutil.virtual_memory()
        if c_load >= 75 or m_load >= 75:
            n = len(psutil.pids())
            c_load/=n
            m_load/=n
            del n
            critical_pids = (i for i in psutil.pids() if (self.handler.cpu_percent(i)<c_load and self.handler.cpu_percent(i)<m_load))
            critical_names = (psutil.Process(i).name() for i in critical_pids )
            del critical_pids
            return critical_names



"""Monitoring network owerload """

class Network:

    def __init__(self):
        self.connections = psutil.net_if_addrs()
        self.net_handler = psutil.net_io_counters()

    def net_exchange(self):
        netstat = {
            "recv": self.net_handler.packets_recv,
            "send": self.net_handler.packets_sent
                   }
        return netstat

    def network_pids(self):
        nets=(psutil.Process(i).connections() for i in psutil.pids() if psutil.Process(i).connections() != [])
        return nets

    def __repr__(self):
        str(self.net_exchange())

    def __del__(self):
        del self.connections
        del self.net_handler

#class MonitorProcessPriority: