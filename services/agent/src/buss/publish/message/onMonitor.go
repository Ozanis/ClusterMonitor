package message

import (
	. "core"
	. "service"
	. "stat"
	. "time"
)

type OnMonitor struct {
	TimeStamp Time       `json:"time_stamp"`
	Cpu       CpuStat    `json:"cpu"`
	Load      LoadStat   `json:"load"`
	Ram       RamStat    `json:"ram"`
	Disk      DiskStat   `json:"disk"`
	Net       []NetStat  `json:"net"`
	User      []UserStat `json:"user"`
}

func MonitorMessage(cpu, load, ram, disk, net, user string, timeout Duration) OnMonitor {
	return OnMonitor{
		TimeStamp: Now(),
		Cpu:       CpuService(ReadFromFileTwice(cpu, timeout)),
		Load:      LoadService(ReadFromFile(load)),
		Ram:       RamService(ram),
		Disk:      DiskService(disk),
		Net:       NetService(net),
		User:      UserService(user),
	}
}

func MapMonitor(message OnMonitor) {

}
