deps=grafana
URL=https://dl.grafana.com/oss/release
package=grafana-7.4.3.linux-amd64.tar.gz

install:
	wget $(URL)/$(package)
	tar -zxvf $(package) -o /tmp/grafana

launch:
	systemctl enable grafana-server \
	&& systemctl daemon-reload \
	&& systemctl start grafana-server \
	&& systemctl status grafana-server

clean:
	rm -vrf /tmp/grafana

deploy: install launch clean