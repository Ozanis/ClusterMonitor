#!/usr/bin/env bash

cd - && cd console && bash outlook.sh

apt purge hexchat
apt purge thunderbird
apt purge compiz-core

apt upgrade

apt install build-essential
apt install libnotify-bin
apt install openjdk-8-jdk -y
apt install preload

apt purge laptop-mode-tools
add-apt-repository -y ppa:linrunner/tlp
apt update
apt install tlp tlp-rdw
tlp start

echo "
vm.swapiness =10
vm.dirty_bytes = 2097152
vm.dirty_background_bytes = 2097152
vm.vfs_cache_pressure = 500" >> /etc/sysctl.conf

echo"
tmpfs /tmp tmpfs defaults,size=2G,mode=1777	0	0" >> /etc/fstab

if [`cat /proc/sys/kernel/sched_autogroup_enabled`];
then echo >> "\nkernel.sched_autogroup_enabled=1"
else break
fi 

systemctl disable systemd-journal-flush.service
systemctl disable openvpn.service
systemctl disable pppd-dns.service
systemctl disable ModemManager.service
systemctl disable speech-dispatcher.service
systemctl disable cgmanager.service
systemctl disable NetworkManager-wait-online.service 

apt autoremove
apt autoclean

journalctl --vacuum-time=5d

systemd-analyze

exit 0
