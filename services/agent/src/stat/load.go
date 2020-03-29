package stat

import (
	"strings"
)

type LoadStat struct {
	Load  string `json:"load"`
	Total string `json:"total"`
}

func MapData(data []string) LoadStat {
	return LoadStat{
		strings.Join([]string{data[0], data[1], data[2]}, " "),
		data[4],
	}
}

func CollectLoad(stream string) LoadStat {
	return MapData(strings.Fields(stream))
}
