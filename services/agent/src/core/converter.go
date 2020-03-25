package core

import (
	"math"
	"strconv"
)

const Gb = float64(1024 * 1024)

func ToGb(num uint64) float64 {
	return float64(num) / Gb
}

func Round3(num float64) float64 {
	return math.Round(1000*num) / 1000
}

func StringToUint(stream string) uint64 {
	ret, _ := strconv.ParseUint(stream, 10, 64)
	return ret
}
