import sys, argparse
from tools import debug_test_tools


class Console:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Using console commands to manage DF-service", add_help=True, prog="DF-service")
        self.parser.add_argument(const="MAN", dest="--man", nargs="?", help="To view program`s summary")
        self.parser.add_argument(const="LOG", dest="--log", nargs="?", help=" To view log")
        self.parser.add_argument(const="SUPPORT", dest="--support", nargs="?", help="To write your exception into log")
        self.parser.add_argument(const="DSBL", dest="--dsbl", nargs="?", help="Disable process extra-autotermination")
        self.parser.add_argument(const="RESTORE", dest="--restore", nargs="?", help="To reject df-patches (optimisations) and restore linux (please use it only in case of your OS`s problem working)")
        self.parser.add_argument(const="DF", dest="--DF!", nargs="?", help="Transform your linux to DF-linux (usually executing on installing service)")

    @debug_test_tools.timer
    @debug_test_tools.check_ram
    @debug_test_tools.check_cpu
    def parse(self):
        return self.parser.parse_args(sys.argv[1:])


c = Console()

c.parse()
