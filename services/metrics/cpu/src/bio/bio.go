package bio

import (
	"bufio"
	"os"
)

func ReadFromFile(fileName string) bufio.Scanner {
	file, _ := os.Open(fileName)
	defer file.Close()
	return *bufio.NewScanner(file)
}
