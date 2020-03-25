package service

import (
	"core"
	"stat/ram"
)

func CollectRam(filename string) ram.Ram {
	return ram.GetMemory(ram.ParseStats(core.ReadFromFile(filename)))
}
