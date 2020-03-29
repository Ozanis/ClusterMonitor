package stat

import (
	"core"
)

type Traffic struct {
	Bytes   uint64 `json:"bytes"`
	Err     uint64 `json:"err"`
	Drp     uint64 `json:"drp"`
	Packets uint64 `json:"packets"`
}

type NetStat struct {
	Name string  `json:"name"`
	Rx   Traffic `json:"rx"`
	Tx   Traffic `json:"tx"`
}

func ParseNetName(stream string) string {
	return stream[:len(stream)-1]
}

func CollectNet(stream []string) NetStat {
	return NetStat{
		Name: ParseNetName(stream[0]),
		Rx: Traffic{
			Bytes: core.StringToUint(stream[1]),
			Err:   core.StringToUint(stream[3]),
			Drp:   core.StringToUint(stream[4]),
		},
		Tx: Traffic{
			Bytes:   core.StringToUint(stream[8]),
			Err:     core.StringToUint(stream[11]),
			Packets: core.StringToUint(stream[12]),
		},
	}
}
