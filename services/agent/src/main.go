package main

import (
	"core"
	"fmt"
	. "service"
)

const (
	timeout   = 1
	usageFile = "/proc/stat"
	loadFile  = "/proc/loadavg"
	ramFile   = "/proc/meminfo"
	diskFile  = "/proc/diskstats"
	netFile   = "/proc/net/dev"
)

func main() {

	for {
		cpu := CpuService(core.ReadFromFileTwice(usageFile, timeout))
		fmt.Println(cpu)

		load := LoadService(core.ReadFromFile(loadFile))
		fmt.Println(load)

		ram := RamService(core.ReadFromFile(ramFile))
		fmt.Println(ram)

		disk := DiskService(core.ReadFromFile(diskFile))
		fmt.Println(disk)

		net := NetService(core.ReadFromFile(netFile))
		fmt.Println(net)
	}
}
