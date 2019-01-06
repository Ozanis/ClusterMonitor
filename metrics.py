import psutil, os, datetime, subprocess

"""Getting SWAP using"""


class SwapMemory:
    def __init__(self):
        self.swap_obj = psutil.swap_memory()

    def swap_used(self):
        return self.swap_obj[1] << 30

    def swap_all(self):
        return self.swap_obj[0] << 30

    def percent(self):
        return self.swap_obj[3]

    def __del__(self):
        del self.swap_obj


"""Getting RAM using"""


class VirtualMemory:

    def __init__(self):
        self.ram_obj = psutil.virtual_memory()

    def ram_tot(self):
        return self.ram_obj[0] << 30

    def ram_used(self):
        return self.ram_obj[3] << 30

    def ram_us_p(self):
        return self.ram_obj[2]

    def __repr__(self):
        return "/".join([self.ram_tot(), self.ram_used(), self.ram_us_p()])

    def __del__(self):
        del self.ram_obj


"""Monitoring sensors"""


class Hardware:

    def __init__(self):
        self.boot = datetime.datetime.fromtimestamp(psutil.boot_time())

    def power(self):
        return psutil.sensors_battery()

    def fans(self):
        return psutil.sensors_fans()

    def temp(self):
        return psutil.sensors_temperatures(fahrenheit=False)

    def __repr__(self):
        return

    def __del__(self):
        del self.boot


"""Boot loading stat"""


class Booting:

    def __init__(self):
        self.time = datetime.datetime.fromtimestamp(psutil.boot_time())

    def time_stat(self):
        return subprocess.check_output(["systemd-analyze"])

    def loading(self):
        return subprocess.check_output(["systemd-analyze", "blame"], universal_newlines=True)

    def __repr__(self):
        return str(self.time_stat())+"\n"+self.loading()

    def __del__(self):
        del self.time

"""CPU working state"""


class Processor:

    def __init__(self):
        self.cpu_stat = {
            "count_physical": psutil.cpu_count(logical=False),
            "count_logical": psutil.cpu_count(logical=True),
            "per_core_usage": psutil.cpu_percent(interval=0.125, percpu=True),
        }

    def __repr__(self):
        return str(self.cpu_stat)

    def __del__(self):
        del self.cpu_stat


"""Monitoring processes"""


class Prcss:

    def __init__(self):
        self.handler = psutil.Process()
        self.dir = str(os.getcwd())

    def proc_log(self):
        proc = {p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])}
        with open("/home/max/Projects/DF_service/logs/proc_log.txt", "w") as _f:
            _f.write(str(proc))

    def critical_prcss(self):
        c_load=psutil.cpu_percent()
        m_load=psutil.virtual_memory()[2]
        if c_load >= 75 or m_load >= 75:
            n = len(psutil.pids())
            c_load/=n
            m_load/=n
            del n
            critical_pids = [i for i in psutil.pids() if (self.handler.cpu_percent(i)<c_load and self.handler.cpu_percent(i)<m_load)]
            critical_names = (psutil.Process(i).name() for i in critical_pids )
            del critical_pids


"""Monitoring network owerload """


class Network:

    def __init__(self):
        self.net_handler = psutil.net_io_counters()

    def net_exchange(self):
        netstat = {
            "recv": self.net_handler.packets_recv,
            "send": self.net_handler.packets_sent
                   }
        return netstat

    def network_pids(self):
        return psutil.net_connections()

    def __repr__(self):
        return "\n".join([self.net_exchange(), self.network_pids()])

    def __del__(self):
        del self.net_handler
