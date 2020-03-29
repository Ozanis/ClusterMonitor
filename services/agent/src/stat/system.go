package stat

type SystemStat struct {
	Identifier   string
	KernelV      string
	Arch         string
	OsVendor     string
	VirtType     string
	Host         string
	ip           string
	BootDuration float64
	Uptime       float64
}
