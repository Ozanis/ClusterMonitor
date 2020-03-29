package stat

import (
	. "core"
	"strings"
)

/*MemTotal[0], MemFree[1], MemAvailable[2], Buffers[3], Cached[4], Active[5], Inactive[6], SwapCached[7], SwapTotal[8], SwapFree[9]*/

type RamStat struct {
	Total     float64 `json:"total"`
	Used      float64 `json:"used"`
	SwapTotal float64 `json:"swap_total"`
	SwapUsed  float64 `json:"swap_used"`
}

func ParseRamStats(stream string) []float64 {
	var stats []float64
	data := strings.Split(stream, "\n")
	for _, i := range data[:10] {
		val := StringToUint(strings.Fields(i)[1])
		stats = append(stats, ToGb(val))
	}
	return stats
}

func GetMemory(stats []float64) RamStat {
	return RamStat{
		Total:     Round3(stats[0]),
		Used:      Round3(stats[0] - stats[1] - stats[3] - stats[4]),
		SwapTotal: Round3(stats[8]),
		SwapUsed:  Round3(stats[8] - stats[9]),
	}
}
