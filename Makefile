OS=$(cat /etc/*release | grep DISTRIB_ID | cut -d"=" -f 2)
dependencies="go git curl wget tar gzip"

system:

rsyslog:
	$(MAKE) -C rsyslog

loki:
	$(MAKE) -C loki

prometheus:
	$(MAKE) -C prometheus

grafana:
	$(MAKE) -C grafana

deploy: system rsyslog loki prometheus grafana