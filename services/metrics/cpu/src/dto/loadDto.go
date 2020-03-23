package dto

import (
	"encoding/base64"
	"encoding/json"
	. "stat"
	"strconv"
	"strings"
)

type LoadDto struct {
	procs string
	total uint64
}

func (dto LoadDto) ToDto(stat Load) LoadDto {
	val, _ := strconv.ParseUint(stat.Total, 10, 32)
	return LoadDto{procs: strings.Join([]string{stat.Load1, stat.Load5, stat.Load15}, " "), total: val}
}

func (dto LoadDto) ToString() []string {
	return []string{dto.procs, string(dto.total)}
}

func (dto LoadDto) ToBytes(data []string) []byte {
	ret, _ := json.Marshal(data)
	return ret
}

func (dto LoadDto) ToBase64(cpu []byte) []byte {
	var ret []byte
	base64.StdEncoding.Encode(ret, cpu)
	return ret
}
