package service

import (
	. "stat"
)

func DiskService(path string) Disk {
	return CollectDisk("/")
}
