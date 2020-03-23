package service

import (
	"bufio"
	. "facade"
)

type CpuService struct {
	usage UsageFacade
	load  LoadFacade
}

func (cs *CpuService) New(scanner bufio.Scanner) {
	cs.usage.GetUnits(scanner)
}

func (cs *CpuService) UsageData(scanner0, scanner1 bufio.Scanner) {
	cs.usage.CollectStats(scanner0, scanner1)
	cs.usage.Dto()
}

func (cs *CpuService) LoadData(scanner bufio.Scanner) {
	cs.load.CollectStats(scanner)
	cs.load.Dto()
}
