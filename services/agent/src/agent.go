package main

import (
	. "buss/publish"
	. "buss/publish/message"
	. "core"
	. "encoding/json"
	. "fmt"
)

const (
	timeout    = 1
	cpuFile    = "/proc/stat"
	loadFile   = "/proc/loadavg"
	ramFile    = "/proc/meminfo"
	diskFile   = "/proc/diskstats"
	netFile    = "/proc/net/dev"
	userFile   = ""
	systemFile = ""
)

const (
	monitoring = "monitoring"
	boot       = "boot"
)

const (
	host = "amqp://guest:guest@localhost:5672/"
)

func main() {
	monitoringQueue := InitQueue(monitoring, host)
	bootQueue := InitQueue(boot, host)

	msg := BootMessage(systemFile)
	dto, err := Marshal(msg)
	FailOnError(err, "marshaling error")
	Println(string(dto))
	FailOnError(Publish(dto, boot, bootQueue), "Publishing error")

	FailOnError(err, "Failed to publish a message")
	for {
		msg := MonitorMessage(cpuFile, loadFile, ramFile, diskFile, netFile, userFile, timeout)
		dto, err := Marshal(msg)
		FailOnError(err, "marshaling error")
		Println(string(dto))
		FailOnError(Publish(dto, monitoring, monitoringQueue), "Publishing error")
	}
}
