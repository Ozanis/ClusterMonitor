package cache

import "github.com/streadway/amqp"

func ShouldCache(stats amqp.Delivery) []byte {
	return CheckCache(stats)
}

func CheckCache(stats amqp.Delivery) []byte {
	return make([]byte, 1)
}
