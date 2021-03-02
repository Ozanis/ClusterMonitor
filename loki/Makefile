repo=https://github.com/grafana/loki

install:
	git clone $(repo)

launch:
	systemctl enable loki \
	&& systemctl start loki \
	&& systemctl start promtail \
	&& systemctl status loki

deploy: dependencies launch