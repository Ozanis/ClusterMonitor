package buss

import 	. "github.com/streadway/amqp"


func SetUpQueue(msgType string, amqp Channel) error{
	return amqp.ExchangeDeclare(
		msgType,
		"fanout",
		true,
		false,
		false,
		false,
		nil,
	)
}


func Publish(msg []byte, msgType string, amqp Channel) error {
	return amqp.Publish(
		msgType,
		"",
		false,
		false,
		Publishing{
			ContentType: "text/plain",
			Body:        msg,
		})
}
