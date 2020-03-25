package service

import (
	. "cache"
	. "consumer"
	. "publisher"
)

func ProccedConnection(string publisherUrl) {
	Publish(ShouldCache(<-Consume(publisherUrl)))
}
