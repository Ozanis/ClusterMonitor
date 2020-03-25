package cpu

import (
	"strings"
)

type Load struct {
	Load  string `json:"load"`
	Total string `json:"total"`
}

func MapData(data []string) Load {
	return Load{
		strings.Join([]string{data[0], data[1], data[2]}, " "),
		data[4],
	}
}

func CollectLoad(stream string) Load {
	return MapData(strings.Fields(stream))
}
