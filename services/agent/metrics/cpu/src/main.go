package main

import "cpu/usage"


func main() {
	cpu := usage.Status{}
	cpu.Usage()
	cpu.Print()
}
