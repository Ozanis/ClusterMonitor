import psutil

p = psutil.pids()
for i in p:
    r = psutil.Process(i).name()
    if "bash" in r:


print()