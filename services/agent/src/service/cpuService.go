package service

import . "stat"

func CpuService(stream0, stream1 string) CpuStat {
	return CpuStat{
		Units:   ParseUnits(stream0),
		Percent: GetPercent(stream0, stream1),
	}
}
