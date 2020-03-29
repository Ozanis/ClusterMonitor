package service

import (
	. "core"
	. "stat"
	"strings"
)

func NetService(stream string) []NetStat {
	var nets []NetStat
	data := strings.Split(ReadFromFile(stream), "\n")[2:]
	for net, _ := range data[2:] {
		nets = append(nets, CollectNet(strings.Fields(data[net])))
	}
	return nets
}
