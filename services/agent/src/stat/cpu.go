package stat

import (
	"core"
	"strings"
)

type Usage struct {
	Percent float64 `json:"percent"`
	Units   int     `json:"units"`
}

type Tact struct {
	Total uint64
	Idle  uint64
}

func ParseCpuStats(stream string) []uint64 {
	var ret []uint64
	str := strings.Split(stream, "\n")
	for _, i := range strings.Fields(str[0]) {
		val := core.StringToUint(i)
		ret = append(ret, val)
	}
	return ret
}

func ParseUnits(stream string) int {
	var units = -1
	for _, substr := range strings.Split(stream, "\n") {
		if strings.HasPrefix(substr, "cpu") {
			units++
		}
	}
	return units
}

func GetIdle(stats []uint64) uint64 {
	return stats[3] + stats[4]
}

func GetTotal(stats []uint64) uint64 {
	var ret uint64 = 0
	for i := range stats {
		ret += stats[i]
	}
	return ret
}

func GetTact(stream string) Tact {
	data := ParseCpuStats(stream)
	return Tact{
		Total: GetTotal(data),
		Idle:  GetIdle(data),
	}
}

func GetUsage(tact0, tact1 Tact) Tact {
	return Tact{
		Total: tact0.Total - tact1.Total,
		Idle:  tact0.Idle - tact1.Idle,
	}
}

func Percentage(tact Tact) float64 {
	return float64(tact.Total-tact.Idle) / float64(tact.Total)
}

func GetPercent(stream0, stream1 string) float64 {
	return Percentage(GetUsage(GetTact(stream0), GetTact(stream1)))
}

/*
PrevIdle = previdle + previowait
Idle = idle + iowait

PrevNonIdle = prevuser + prevnice + prevsystem + previrq + prevsoftirq + prevsteal
NonIdle = user + nice + system + irq + softirq + steal

PrevTotal = PrevIdle + PrevNonIdle
Total = Idle + NonIdle

# differentiate: actual value minus the previous one
totald = Total - PrevTotal
idled = Idle - PrevIdle

CPU_Percentage = (totald - idled)/totald
*/
