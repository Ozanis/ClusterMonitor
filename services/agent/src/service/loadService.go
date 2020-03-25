package service

import "stat"

func LoadService(stream string) stat.Load {
	return stat.CollectLoad(stream)
}
