package usage

import (
	. "fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)


type Status struct{
	total float64
	idle float64
	usage float64
}


func getSample() (idle, total uint64) {
	contents, err := ioutil.ReadFile("/proc/stat")
	if err != nil {
		return
	}
	lines := strings.Split(string(contents), "\n")
	for _, line := range lines {
		fields := strings.Fields(line)
		if fields[0] == "cpu" {
			numFields := len(fields)
			for i := 1; i < numFields; i++ {
				val, err := strconv.ParseUint(fields[i], 10, 64)
				if err != nil {
					Println("Error: ", i, fields[i], err)
				}
				total += val
				if i == 4 {
					idle = val
				}
			}
			return
		}
	}
	return
}


func (Cpu * Status) Usage() {
	idle0, total0 := getSample()
	time.Sleep(3 * time.Second)
	idle1, total1 := getSample()
	Cpu.idle = float64(idle1 - idle0)
	Cpu.total = float64(total1 - total0)
	Cpu.usage = 100 * (Cpu.total - Cpu.idle) / Cpu.total
}


func (Cpu * Status) Print() {
	Printf("CPU usage is %f%% [busy: %f, total: %f]\n", Cpu.usage, Cpu.total-Cpu.idle, Cpu.total)
}
