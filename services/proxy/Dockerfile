FROM centos:latest
ENV container docker
RUN yum -y update && yum clean all
RUN yum install golang
RUN go get github.com/streadway/amqp
RUN export GOPATH=/proxy
RUN export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
WORKDIR /proxy
COPY .. ./proxy
RUN go build main.go
ENTRYPOINT ["./main"]