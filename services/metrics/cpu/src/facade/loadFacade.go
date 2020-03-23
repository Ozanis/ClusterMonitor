package facade

import (
	"bufio"
	"dto"
	"stat"
)

type LoadFacade struct {
	dto  dto.LoadDto
	stat stat.Load
}

func (facade *LoadFacade) CollectStats(scanner bufio.Scanner) {
	facade.stat.MapData(facade.stat.ParseData(scanner))
	facade.dto.ToDto(facade.stat)
}

func (facade *LoadFacade) Dto() dto.LoadDto {
	return facade.dto
}
