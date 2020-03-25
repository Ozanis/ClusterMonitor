FROM centos:latest
ENV container docker
RUN yum -y update && yum clean all
RUN yum install golang
RUN export GOPATH=/agent
RUN export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
WORKDIR /agent
COPY .. ./agent
RUN go get github.com/streadway/amqp
RUN go build main.go
EXPOSE 5672
ENTRYPOINT ["./main"]