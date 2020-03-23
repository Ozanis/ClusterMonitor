package stat

import (
	"bufio"
	"strings"
)

type Load struct {
	Load1  string `json:"load1"`
	Load5  string `json:"load5"`
	Load15 string `json:"load15"`
	Fract  string `json:"fract"`
	Total  string `json:"fract"`
}

func (stat *Load) ParseData(scanner bufio.Scanner) []string {
	return strings.Fields(scanner.Text())
}

func (stat *Load) MapData(data []string) {
	stat.Load1 = data[0]
	stat.Load5 = data[1]
	stat.Load15 = data[2]
	stat.Fract = data[3]
	stat.Total = data[4]
}
