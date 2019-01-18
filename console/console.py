import sys, os, subprocess, telemetry_server


def hlp():
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
        if len(msg) > 1:
            sup.send(msg.encode())
            subprocess.Popen(['notify-send', "Message have been sent"])
        else:
            subprocess.Popen(['notify-send', "Error: Very short message"])
    finally:
        exit(0)


def clear():
    drct = "/usr/bin/DF/log/telemetry.log"
    try:
        with open(drct, "w") as _f:
            _f.write("")
    except IOError:
        exit(1)

#def dsbl():

#def restore():


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
 #   elif i == 4:
  #      dsbl()
   # elif i ==5:
    #    restore()
    elif i == 6:
        DF()
    elif i==7:
        help()


if __name__ == "main":
    path = str(os.getcwd())
    arg = parse()
    if arg is None:
        hlp()
    else:
        com(arg)
    exit(0)
