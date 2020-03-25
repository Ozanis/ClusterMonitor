package main

import (
	"bio"
	"fmt"
	. "service"
)

const (
	loadFile  = "/proc/loadavg"
	usageFile = "/proc/stat"
	timeout   = 1
)

func main() {
	cpu := Stat{
		CpuUsage: CpuUsage(bio.ReadFromFileTwice(usageFile, timeout)),
		CpuLoad:  CpuLoad(bio.ReadFromFile(loadFile)),
	}
	fmt.Println(cpu)
}
