package service

import (
	. "core"
	. "stat"
)

func RamService(stream string) RamStat {
	return GetMemory(ParseRamStats(ReadFromFile(stream)))
}
