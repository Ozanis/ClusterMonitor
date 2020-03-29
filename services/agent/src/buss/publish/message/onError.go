package message

import . "time"

type OnError struct {
	Err       string `json:"err"`
	TimeStamp Time   `json:"time_stamp"`
}

func (OnError) ProduceMessage(err error) OnError {
	return OnError{
		Err:       err.Error(),
		TimeStamp: Now(),
	}
}

func MapError(message OnError) {

}
