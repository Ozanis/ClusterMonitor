package main

import (
	. "disk/usage"
)

func main() {
	disk := Status{}
	disk.Usage()
	disk.Print()
}
