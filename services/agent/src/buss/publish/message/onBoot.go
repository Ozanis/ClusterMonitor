package message

import (
	. "service"
	. "stat"
	. "time"
)

type OnBoot struct {
	TimeStamp Time       `json:"time_stamp"`
	Boot      SystemStat `json:"boot"`
}

func BootMessage(stream string) OnBoot {
	return OnBoot{
		TimeStamp: Now(),
		Boot:      SystemService(stream),
	}
}

func MapBoot() {

}
