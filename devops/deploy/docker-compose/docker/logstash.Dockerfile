FROM alpine:latest
RUN apk update && apk upgrade
ENV GOLANG_VERSION 1.4.0
RUN wget -O go.tgz "https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz"; \
    	tar -C /usr/local -xzf go.tgz; \
    	rm go.tgz; \
    	cd /usr/local/go/src; \
        	./make.bash; \
        	\ rm -rf \
COPY ../../../../services ./server
ENV GOPATH ~/server
RUN export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
RUN go get github.com/streadway/amqp && go build server.go
RUN chmod -R 001 "$GOPATH"
WORKDIR /server
ENTRYPOINT ["./src/server"]