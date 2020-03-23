package runtime

import (
	"context"
	"time"
	//"fmt"
)

func runtime() uint64 {
	return time.Now().Unix() - context.Background()
}
