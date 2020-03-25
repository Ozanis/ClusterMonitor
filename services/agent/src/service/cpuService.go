package service

import (
	. "stat/cpu"
)

type Cpu struct {
	CpuUsage Usage
	CpuLoad  Load
}

func CpuUsage(stream0, stream1 string) Usage {
	return Usage{
		Units:   ParseUnits(stream0),
		Percent: GetPercent(stream0, stream1),
	}
}

func CpuLoad(stream string) Load {
	return CollectLoad(stream)
}
