import subprocess
from Agent import metrics
from tools import debug_test_tools


@debug_test_tools.timer
@debug_test_tools.check_ram
@debug_test_tools.check_cpu
def test():
    p= metrics.Prcss().critical_prcss()
    subprocess.Popen(['notify-send', str(p)])

test()