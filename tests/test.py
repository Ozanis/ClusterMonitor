import psutil

procs = [p.pid: p.info for p in psutil.process_iter(attrs=['name', 'username'])
print(procs)