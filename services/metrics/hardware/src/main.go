package main

import (
	. "dynamic/usage"
)

func main() {
	disk := Status{}
	disk.Usage()
	disk.Print()
}
