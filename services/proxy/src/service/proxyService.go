package service

import (
	. "buss"
	 "fmt"
	. "github.com/streadway/amqp"
	 "log"
)


func ConnectBuss(hostURL string) (Connection, error){
	conn, err := Dial(hostURL)
	defer conn.Close()
	return *conn, err
}

func CreateChannel(amqp Connection) (Channel, error) {
	ch, err := amqp.Channel()
	defer ch.Close()
	return *ch, err
}


func FailOnError(err error, warn string) {
	if err != nil {
		fmt.Println("#{msg}: #{err}")
		log.Fatalf("%s: %s", warn, err)
	}
}


func InitQueue(msgType, url string) <-chan Delivery {
	amqp, err := ConnectBuss(url)
	FailOnError(err, "unable connect to AMQP")
	chann, err := CreateChannel(amqp)
	FailOnError(err, "unable to create channel")
	queue, err := DeclareQueue(chann, msgType)
	FailOnError(err, "creating topic error")
	err = BindQueue(chann, queue)
	FailOnError(err, "error binding to queue")
	c, err := SubscribeTopic(chann, queue)
	FailOnError(err, "subscribe error")
	return c
}


func HandleQueue(amqp <-chan Delivery){
	for {
		res := <-amqp
		fmt.Println(res)
	}
}
