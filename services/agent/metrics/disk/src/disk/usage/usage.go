package usage

import (
	. "fmt"
	. "syscall"
)


const (
	B  = 1
	KB = 1024 * B
	MB = 1024 * KB
	GB = 1024 * MB
)


type Status struct {
	All  uint64 `json:"all"`
	Used uint64 `json:"used"`
	Free uint64 `json:"free"`
}


func (Disk * Status) Usage() {
	fs := Statfs_t{}
	err := Statfs("/", &fs)
	if err != nil {
		return
	}
	Disk.All = fs.Blocks * uint64(fs.Bsize)
	Disk.Free = fs.Bfree * uint64(fs.Bsize)
	Disk.Used = Disk.All - Disk.Free
}


func (Disk * Status) Print(){
	Printf("All: %.2f GB\n", float64(Disk.All)/float64(GB))
	Printf("Used: %.2f GB\n", float64(Disk.Used)/float64(GB))
	Printf("Free: %.2f GB\n", float64(Disk.Free)/float64(GB))
}
