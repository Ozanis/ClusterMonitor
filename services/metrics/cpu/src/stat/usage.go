package stat

import (
	"bufio"
	"strconv"
	"strings"
	"unicode"
)

type Usage struct {
	Total, Units, idle uint64
	tags               map[string]uint64
}

func (cpu *Usage) New() {
	cpu.tags = map[string]uint64{
		"user":       0,
		"nice":       0,
		"system":     0,
		"idle":       0,
		"iowait":     0,
		"irq":        0,
		"softirq":    0,
		"steal":      0,
		"guest":      0,
		"guest_nice": 0,
	}
}

func (cpu *Usage) ParseStats(stream string) {
	fields := strings.Fields(stream[1:])
	for _, valStr := range fields {
		val, _ := strconv.ParseUint(valStr, 10, 64)
		cpu.tags[valStr] = val
	}
}

func (cpu *Usage) ParseUnits(stream bufio.Scanner) {
	for stream.Scan() {
		line := stream.Text()
		if strings.HasPrefix(line, "cpu") && unicode.IsDigit(rune(line[3])) {
			cpu.Units++
		}
	}
}

func (cpu *Usage) GetIdle() uint64 {
	cpu.idle = cpu.tags["idle"] + cpu.tags["iowait"]
	return cpu.idle
}

func (cpu *Usage) GetTotal() uint64 {
	cpu.Total = cpu.tags["user"] + cpu.tags["nice"] + cpu.tags["system"] + cpu.tags["irq"] + cpu.tags["softirq"] + cpu.tags["steal"] + cpu.idle
	return cpu.Total
}

func (cpu *Usage) Percentage() float64 {
	return float64(100*(cpu.Total-cpu.idle)) / float64(cpu.Total)
}
