package core

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"time"
)

func ReadFromFile(fileName string) string {
	file, err := ioutil.ReadFile(fileName)
	if err != nil {
		fmt.Println(fmt.Errorf("%w", err))
	}
	return string(file)
}

func ReadFromFileTwice(fileName string, duration time.Duration) (string, string) {
	stream0 := ReadFromFile(fileName)
	time.Sleep(duration * time.Second)
	stream1 := ReadFromFile(fileName)
	return stream0, stream1
}

func Bytes(data []string) ([]byte, error) {
	return json.Marshal(data)
}
