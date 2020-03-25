package consumer

import (
	. "core"
	"github.com/streadway/amqp"
)

func Consume(publisherUrl string) <-chan amqp.Delivery {
	conn, err := amqp.Dial(publisherUrl)
	FailOnError(err, "Failed to connect to RabbitMQ")
	defer conn.Close()

	ch, err := conn.Channel()
	FailOnError(err, "Failed to open a channel")
	defer ch.Close()

	err = ch.ExchangeDeclare(
		"stats",
		"fanout",
		true,
		false,
		false,
		false,
		nil,
	)
	FailOnError(err, "Failed to declare an exchange")

	q, err := ch.QueueDeclare(
		"",
		false,
		false,
		true,
		false,
		nil,
	)
	FailOnError(err, "Failed to declare a queue")

	err = ch.QueueBind(
		q.Name,
		"",
		"stats",
		false,
		nil)
	FailOnError(err, "Failed to bind a queue")

	msgs, err := ch.Consume(
		q.Name,
		"",
		true,
		false,
		false,
		false,
		nil,
	)
	FailOnError(err, "Failed to register a consumer")
	/*
		forever := make(chan bool)

		go func() {
			for d := range msgs {
				log.Printf(" [x] %s", d.Body)
			}
		}()

		log.Printf("Awaiting stats")
		<-forever
	*/
	return msgs
}
