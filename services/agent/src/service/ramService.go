package service

import (
	"stat"
)

func RamService(stream string) stat.Ram {
	return stat.GetMemory(stat.ParseStats(stream))
}
