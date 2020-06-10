package main

import . "service"

const ServerUrl = "amqp://guest:guest@localhost:5672/"

const (
	monitoring = "monitoring"
	boot 	   = "boot"
	err 	   = "error"
)


func main(){
	bootChannel := InitQueue(boot, ServerUrl)
	monitoringChannel := InitQueue(monitoring, ServerUrl)
	go HandleQueue(bootChannel)
	go HandleQueue(monitoringChannel)
}
