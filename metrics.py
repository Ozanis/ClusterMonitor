import psutil, os, datetime, subprocess, logging

"""Getting SWAP using"""


class SwapMemory:
    def __init__(self):
        self.swap_obj = psutil.swap_memory()

    def __repr__(self):
        return str({
            "all_swap": self.swap_obj[0] << 30,
            "used": self.swap_obj[1] << 30,
            "%": self.swap_obj[3]
        })

    def __del__(self):
        del self.swap_obj


"""Getting RAM using"""


class VirtualMemory:

    def __init__(self):
        self.ram_obj = psutil.virtual_memory()

    def __repr__(self):
        return str({"ram_tot": self.ram_obj[0] << 30, "ram_used":self.ram_obj[3] << 30, "%": self.ram_obj[2]})

    def __del__(self):
        del self.ram_obj


"""Monitoring sensors"""


class Hardware:

    def __init__(self):
        self.power = psutil.sensors_battery()
        self.fans = psutil.sensors_fans()
        self.temp = psutil.sensors_temperatures(fahrenheit=False)

    def __repr__(self):
        return "\n".join([self.power, self.fans, self.temp])

    def __del__(self):
        del self.power
        del self.fans
        del self.temp


"""Boot loading stat"""


class Booting:

    def __init__(self):
        self.time = datetime.datetime.fromtimestamp(psutil.boot_time())

    @staticmethod
    def system_log():
        subprocess.check_output(["systemd-analyze", "blame"], universal_newlines=True)
        subprocess.check_output(["systemd-analyze"])
        subprocess.check_output(["uname", "-a"], universal_newlines=True)

    def __repr__(self):
        return str(self.time) + "\n" + str(self.system_log())

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

    def critical_prcss(self):
        c_load=psutil.cpu_percent()
        m_load=psutil.virtual_memory()[2]
        if c_load >= 75 or m_load >= 75:
            n = len(psutil.pids())
            c_load /= n
            m_load /= n
            del n
            critical_pids = [i for i in psutil.pids() if (self.handler.cpu_percent(i)<c_load and self.handler.cpu_percent(i)<m_load)]
            critical_names = [psutil.Process(i).name() for i in critical_pids]
            del critical_pids
            critical_processes = "Critical processes:"+ str(critical_names)
            subprocess.Popen(['notify-send', critical_processes])

    def __repr__(self):
        return str({p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])})


"""Monitoring network owerload """


class Network:

    def __init__(self):
        self.net_handler = psutil.net_io_counters()

    def __repr__(self):
        net_stat = {
            "recv": self.net_handler.packets_recv,
            "send": self.net_handler.packets_sent
        }
        return str("\n".join([net_stat, psutil.net_connections()]))

    def __del__(self):
        del self.net_handler


"""Realise telemetry collection and logging"""


class Telemetry(SwapMemory, VirtualMemory, Hardware, Booting, Processor, Prcss, Network):

    def __init__(self):
        super().__init__()
        logging.basicConfig(filename=str(os.getcwd()) + "/logs/telemetry_log.log", level=logging.INFO)

    @staticmethod
    def to_do_logs():
        try:
            logging.info("---Boot log---")
            logging.info(Booting())
            logging.info("---Hardware log---")
            logging.info(Hardware())
            logging.info("---CPU log---")
            logging.info(Processor())
            logging.info("---RAM log---")
            logging.info(VirtualMemory())
            logging.info("---SWAP using log---")
            logging.info(SwapMemory())
            logging.info("---Process log---")
            logging.info(Prcss())
            logging.info("---Network log---")
        except RuntimeError:
            logging.warning("UNABLE TO WRITE LOG")
            subprocess.Popen(['notify-send', "Error: Unable to write telemetry data"])
