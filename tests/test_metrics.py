import psutil, os, debug_test_tools, metrics

def sensors_stat():
    hrdw = metrics.Hardware()
    print(hrdw.boot)
    print(hrdw.__repr__())

def ram_stat():
    ram = metrics.VirtualMemory()
    print(ram.__repr__())

def cpu_stat():
    cpu = metrics.Processor()
    print(cpu.__repr__())

def proc_stat():
    proc = metrics.Prcss()
    print(proc.__repr__())

def net_stat():
    net = metrics.Network()
    print(net.__repr__())

@debug_test_tools.timer
@debug_test_tools.check_ram
@debug_test_tools.check_cpu
def test():
    sensors_stat()
    ram_stat()
    cpu_stat()
    proc_stat()
    net_stat()

test()