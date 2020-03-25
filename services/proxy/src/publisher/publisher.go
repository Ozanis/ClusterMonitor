package publisher

import (
	. "core"
	"github.com/streadway/amqp"
	"log"
)

const ServerUrl = "amqp://guest:guest@localhost:5672/"

func Publish(data []byte) {
	conn, err := amqp.Dial(ServerUrl)
	FailOnError(err, "Failed to connect to server")
	defer conn.Close()

	ch, err := conn.Channel()
	FailOnError(err, "Failed to open a channel")
	defer ch.Close()

	err = ch.ExchangeDeclare(
		"logs",
		"fanout",
		true,
		false,
		false,
		false,
		nil,
	)
	FailOnError(err, "Failed to declare an exchange")

	body := data
	err = ch.Publish(
		"stats",
		"",
		false,
		false,
		amqp.Publishing{
			ContentType: "text/plain",
			Body:        body,
		})
	FailOnError(err, "Failed to publish a message")

	log.Printf(" [x] Sent %s", body)
}
