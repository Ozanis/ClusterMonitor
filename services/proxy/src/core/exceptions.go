package core

import (
	"fmt"
	"log"
)

func FailOnError(err error, msg string) {
	if err != nil {
		fmt.Println("#{msg}: #{err}")
		log.Fatalf("%s: %s", msg, err)
	}
}
