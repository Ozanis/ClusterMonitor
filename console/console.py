import sys, os, subprocess, telemetry_server
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

def help():
    try:
        with open(path+"help.txt") as _f:
            print(_f.read())
    except IOError:
        exit(1)

def man():
    try:
        with open(path+"man.txt") as _f:
            print(_f.read())
    except IOError:
        exit(1)

def log():
    drct="/usr/bin/DF/log/telemetry.log"
    try:
        with open(drct) as _f:
            print(_f.read())
    except IOError:
        exit(1)

def support():
    sup = telemetry_server.SockSsl()
    print("Your exceptions:\n")
    msg = str(input())
    try:
        sup.send(msg.encode())
    finally:
        exit(0)

def clear():
    drct = "/usr/bin/DF/log/telemetry.log"
    try:
        with open(drct, "w") as _f:
            _f.write("")
    except IOError:
        exit(1)

def dsbl():

def restore():

def DF():
    subprocess.call(path+"outlook.sh", shell=True)


def parse():
    cmd = str(input())
    propereties = ("man", "log", "support", "clear", "dsbl", "restore", "DF", "help")
    if cmd in propereties:
        for i in range(len(propereties)):
            if propereties[i]==cmd:
                return i
    else:
        return None

def com(i):
    if i ==0:
        man()
    elif i ==1:
        log()
    elif i == 2:
        support()
    elif i == 3:
        clear()
    elif i == 4:
        dsbl()
    elif i ==5:
        restore()
    elif i == 6:
        DF()
    elif i==7:
        help()


if __name__ == "main":
    path = str(os.getcwd())
    arg = parse()
    if arg is None:
        help()
    else:
        com(arg)
    exit(0)