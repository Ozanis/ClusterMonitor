package stat

import (
	. "core"
	"fmt"
	"syscall"
)

type DiskStat struct {
	//	Name       string  `json:"name"`
	Capacity float64 `json:"capacity"`
	Usage    float64 `json:"used"`
	//	Reads      uint64  `json:"read"`
	//	Writes     uint64  `json:"write"`
	//	Inodes	   float64 `json:"inodes"`
}

func GetDiskDescriptor(path string) syscall.Statfs_t {
	fs := syscall.Statfs_t{}
	err := syscall.Statfs(path, &fs)
	if err != nil {
		fmt.Println("unable to get disk descriptor")
	}
	return fs
}

func GetDiskCapacity(fs syscall.Statfs_t) uint64 {
	return fs.Blocks * uint64(fs.Bsize)
}

func GetDiskFreeSpace(fs syscall.Statfs_t) uint64 {
	return fs.Bfree * uint64(fs.Bsize)
}

func DiskPercent(capacity, usage uint64) float64 {
	return float64(usage) / float64(capacity) * 100
}

func CollectDisk(path string) DiskStat {
	desc := GetDiskDescriptor(path)
	capacity := GetDiskCapacity(desc)
	return DiskStat{
		Capacity: Round3(ToGb(capacity / 1024)),
		Usage:    Round3(DiskPercent(capacity, GetDiskFreeSpace(desc))),
	}
}
