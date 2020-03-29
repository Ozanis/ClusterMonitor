package service

import . "stat"

func SystemService(stream string) SystemStat {
	return SystemStat{
		Identifier:   "",
		KernelV:      "",
		Arch:         "",
		OsVendor:     "",
		VirtType:     "",
		Host:         "",
		BootDuration: 0,
		Uptime:       0,
	}
}
