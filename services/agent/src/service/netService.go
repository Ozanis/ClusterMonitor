package service

import (
	. "stat"
	"strings"
)

func NetService(stream string) []Net {
	var nets []Net
	data := strings.Split(stream, "\n")[2:]
	for net, _ := range data[2:] {
		nets = append(nets, CollectNet(strings.Fields(data[net])))
	}
	return nets
}
