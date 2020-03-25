package src

import . "service"

const publisherUrl = "amqp://guest:guest@localhost:5672/"

func main() {
	ProccedConnection(publisherUrl)
}
