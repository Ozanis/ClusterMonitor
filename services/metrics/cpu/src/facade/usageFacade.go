package facade

import (
	"bufio"
	"dto"
	"stat"
)

type UsageFacade struct {
	dto  dto.UsageDto
	stat stat.Usage
}

func (facade *UsageFacade) GetUnits(data bufio.Scanner) {
	facade.stat.ParseUnits(data)
}

func (facade *UsageFacade) getTact(data bufio.Scanner) (uint64, uint64) {
	facade.stat.ParseStats(data.Text())
	return facade.stat.GetTotal(), facade.stat.GetIdle()
}

func (facade *UsageFacade) CollectStats(data0, data1 bufio.Scanner) {
	facade.getTact(data0)
	facade.getTact(data1)
	facade.dto.Percent = facade.stat.Percentage()
}

func (facade *UsageFacade) Dto() dto.UsageDto {
	return facade.dto
}
