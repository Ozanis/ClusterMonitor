package stat

type Proc struct {
	Name string  `json:"num"`
	Cpu  float64 `json:"cpu"`
	Ram  float64 `json:"ram"`
	File string  `json:"file"`
	Sock uint64  `json:"sock"`
}

type UserStat struct {
	Id    uint64 `json:"id"`
	Name  string `json:"name"`
	Num   uint64 `json:"num"`
	Procs []Proc `json:"procs"`
}
