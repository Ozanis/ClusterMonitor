package main

import (
	"bio"
	. "service"
)

const (
	loadFile  = "/proc/loadavg"
	usageFile = "/proc/stat"
)

func main() {
	usage := bio.ReadFromFile(usageFile)
	load := bio.ReadFromFile(loadFile)

	cpu := service.CpuService{}
	cpu.New(usage)
	cpu.LoadData(load)
	cache := bio.ReadFromFile(usageFile)
	cpu.UsageData(usage, cache)
}
