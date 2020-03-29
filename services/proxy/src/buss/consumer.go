package buss

import . "github.com/streadway/amqp"


func Subscribe(amqp Channel) error {
	return amqp.ExchangeDeclare(
		"src",
		"fanout",
		true,
		false,
		false,
		false,
		nil,
	)
}

func DeclareQueue(amqp Channel, name string) (Queue, error){
	return amqp.QueueDeclare(
		name,
		false,
		false,
		true,
		false,
		nil,
	)
}

func BindQueue(amqp Channel, queue Queue) error{
	return amqp.QueueBind(
		queue.Name,
		"",
		"src",
		false,
		nil)
}

func SubscribeTopic(amqp Channel, queue Queue) (<-chan Delivery, error){
	return amqp.Consume(
		queue.Name,
		"",
		true,
		false,
		false,
		false,
		nil,
	)
}
