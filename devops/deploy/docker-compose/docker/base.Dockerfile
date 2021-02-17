FROM alpine:latest
ARG rabbit_v="3.6.1"
ARG go_v="1.14.0"
ENV RABBITMQ_VERSION=rabbit_v
ENV GOLANG_VERSION=go_v
RUN apk add --update --no-cache wget tar xz bash erlang erlang-mnesia erlang-public-key erlang-crypto erlang-ssl erlang-sasl erlang-asn1 erlang-inets erlang-os-mon erlang-xmerl erlang-eldap erlang-syntax-tools
RUN wget https://www.rabbitmq.com/releases/rabbitmq-server/v${RABBITMQ_VERSION}/rabbitmq-server-generic-unix-${RABBITMQ_VERSION}.tar.xz | tar -xJ -C / --strip-components 1 && rm -rf /share/**/rabbitmq*.xz
RUN apk del --purge wget tar xz
RUN addgroup rabbitmq
RUN adduser -DS -g "" -G rabbitmq -s /bin/sh -h /var/lib/rabbitmq rabbitmq
RUN mkdir -p /data/rabbitmq
RUN chown -R rabbitmq:rabbitmq /data/rabbitmq
ENV PATH /usr/lib/rabbitmq/bin:$PATH
LABEL name="RabbitMQ image"
#RUN rabbitmq-diagnostics status
#RUN rabbitmq-plugins enable rabbitmq_management
RUN wget -O go.tgz "https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz"
RUN tar -C /usr/local -xzf go.tgz && rm go.tgz
RUN	cd /usr/local/go/src && ./make.bash && rm -rf
COPY ./"$SERVICE" ./"$SERVICE"
ENV GOPATH ~/"$SERVICE"
RUN export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
RUN go get github.com/streadway/amqp && go build "$SERVICE".go
LABEL name="Ready $SERVICE image"
WORKDIR /"$SERVICE"
#RUN chmod -R 555 "$SERVICE"
RUN rabbitmq-server -detached
ENTRYPOINT ["./$SERVICE"]
