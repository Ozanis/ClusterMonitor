package service

import (
	"stat"
)

func CpuService(stream0, stream1 string) stat.Usage {
	return stat.Usage{
		Units:   stat.ParseUnits(stream0),
		Percent: stat.GetPercent(stream0, stream1),
	}
}
