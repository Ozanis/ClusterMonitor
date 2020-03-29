package service

import . "stat"

func LoadService(stream string) LoadStat {
	return CollectLoad(stream)
}
