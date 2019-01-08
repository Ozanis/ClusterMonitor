import debug_test_tools, psutil
from dataclasses import field, dataclass

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


@dataclass
class Hardware:

    power: str = field(default=psutil.sensors_battery(), repr=True)
    fans: str = field(default=psutil.sensors_fans(), repr=True)
    temp: str = field(default=psutil.sensors_temperatures(fahrenheit=False), repr=True)

    def __repr__(self):
        return "\n".join([self.power, self.fans, self.temp])

    def __del__(self):
        del self.power
        del self.fans
        del self.temp

