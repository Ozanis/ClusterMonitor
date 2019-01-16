import subprocess, psutil, metrics, time
import sys
#import argparse
#parser = argparse.ArgumentParser(description="Using console commands to manage DF-service", add_help=True, prog="DF-service")
#parser.add_argument(const="MAN", dest="--man", nargs="?", help="To view program`s summary")
#parser.add_argument(const="LOG", dest="--log", nargs="?", help=" To view log")
#parser.add_argument(const="SUPPORT", dest="--support", nargs="?", help="To write your exception into log")
#parser.add_argument(const="CLEAR", dest="--clear", nargs="?", help="Clear log")
#parser.add_argument(const="DSBL", dest="--dsbl", nargs="?", help="Disable process extra-autotermination")
#parser.add_argument(const="RESTORE", dest="--restore", nargs="?", help="To reject df-patches (optimisations) and restore linux (please use it only in case of your OS`s problem working)")
#parser.add_argument(const="DF", dest="--DF!", nargs="?", help="Transform your linux to DF-linux (usually executing on installing service)")
#parser.parse_args(sys.argv[1:])


def call():
    pids = psutil.pids()
    d=len(pids)
    for p in pids:
        r = psutil.Process(p).name()
        if r == "bash":
            return p
        elif p == d:
            return None


def activate(p):
    if p != None:
        time.sleep(0.75)
        print("bash")
        return psutil.Process(p).is_running()
    else:
        pass

def parser():
    pipe = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    check_input = pipe.communicate(input=input())
    propereties = ("-man", "-log", "-support", "-clear", "-dsbl", "-restore", "-DF", "-help", "-h")
    for i in check_input:
        print(i)


def console():
    while True:
        val = call()
        if activate(val):
            print("start")
            parser()

console()
