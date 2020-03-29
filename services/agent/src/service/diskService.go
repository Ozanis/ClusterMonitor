package service

import (
	. "stat"
)

func DiskService(path string) DiskStat {
	return CollectDisk("/")
}
