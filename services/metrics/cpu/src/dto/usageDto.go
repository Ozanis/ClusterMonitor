package dto

import (
	"encoding/base64"
	"encoding/json"
)

type UsageDto struct {
	Percent float64 `json:"percent"`
	Units   uint64  `json:"units"`
}

func (dto UsageDto) ToBytes(data []string) []byte {
	ret, _ := json.Marshal(data)
	return ret
}

func (dto UsageDto) ToBase64(cpu []byte) []byte {
	var ret []byte
	base64.StdEncoding.Encode(ret, cpu)
	return ret
}
