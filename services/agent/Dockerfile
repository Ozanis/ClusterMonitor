
FROM centos:latest
ENV container docker
RUN yum -y update && yum clean all
RUN yum install golang
RUN export GOPATH=/agent
RUN export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin
WORKDIR /agent
COPY .. ./agent
RUN go build main.go
ENTRYPOINT ["./main"]