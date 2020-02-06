#!/usr/bin/sh

ps -o pid,user,%mem,command ax | sort -b -k3 -r

exit 0
