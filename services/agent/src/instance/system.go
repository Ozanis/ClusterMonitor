package instance

type System struct {
	Identifier    string
	KernelV       string
	Arch          string
	OsVendor      string
	VirtType      string
	Host          string
	ip            string
	BootTimestamp float64
	BootDuration  float64
	Uptime        float64
}
