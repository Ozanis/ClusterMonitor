import sys, argparse

parser = argparse.ArgumentParser(description="Using console commands to manage DF-service", add_help=True, prog="DF-service")
parser.add_argument(const="MAN", dest="--man", nargs="?", help="To view program`s summary")
parser.add_argument(const="LOG", dest="--log", nargs="?", help=" To view logs")
parser.add_argument(const="SUPPORT", dest="--support", nargs="?", help="To write your exception into logs")
parser.add_argument(const="CLEAR", dest="--clear", nargs="?", help="Clear logs")
parser.add_argument(const="DSBL", dest="--dsbl", nargs="?", help="Disable process extra-autotermination")
parser.add_argument(const="RESTORE", dest="--restore", nargs="?", help="To reject df-patches (optimisations) and restore linux (please use it only in case of your OS`s problem working)")
parser.add_argument(const="DF", dest="--DF!", nargs="?", help="Transform your linux to DF-linux (usually executing on installing service)")
parser.parse_args(sys.argv[1:])
