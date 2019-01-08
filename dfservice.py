import sys, telemetry_server, controller, metrics, threading

"""Main script"""

def get_telemetry():
    hrdw = metrics.Hardware()
    ram = metrics.VirtualMemory()
    cpu = metrics.Processor()
    prcss = metrics.Prcss()
    net = metrics.Network()
    boot = metrics.Booting()
    swap = metrics.SwapMemory
    telemetry = metrics.Telemetry()
    telemetry.to_do_logs()

get_telemetry()