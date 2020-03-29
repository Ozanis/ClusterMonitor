package publish

import (
	. "core"
	. "github.com/streadway/amqp"
)

func ConnectBuss(hostURL string) (Connection, error) {
	conn, err := Dial(hostURL)
	defer conn.Close()
	return *conn, err
}

func CreateChannel(amqp Connection) (Channel, error) {
	ch, err := amqp.Channel()
	defer ch.Close()
	return *ch, err
}

func SetUpQueue(msgType string, amqp Channel) error {
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

func InitQueue(msqType, url string) Channel {
	amqp, err := ConnectBuss(url)
	FailOnError(err, "unable connect to AMQP")
	chann, err := CreateChannel(amqp)
	FailOnError(err, "unable to create channel")
	FailOnError(SetUpQueue(msqType, chann), "creating topic error")
	return chann
}
