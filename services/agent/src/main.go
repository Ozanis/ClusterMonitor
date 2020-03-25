package main

import (
	"core"
	"fmt"
	. "service"
)

const (
	loadFile  = "/proc/loadavg"
	usageFile = "/proc/stat"
	ramFile   = "/proc/meminfo"
	timeout   = 1
)

func main() {
	cpu := Cpu{
		CpuUsage: CpuUsage(core.ReadFromFileTwice(usageFile, timeout)),
		CpuLoad:  CpuLoad(core.ReadFromFile(loadFile)),
	}
	fmt.Println(cpu)
	ram := CollectRam(ramFile)
	fmt.Println(ram)

}
