exporters=prometheus-node-exporter prometheus-alertmanager prometheus-mysqld-exporter prometheus-process-exporter

download_path=/tmp
version=2.25.0
artifacts=prometheus-$(version).linux-amd64
package=$(artifacts).tar.gz
URL=https://github.com/prometheus/prometheus/releases/download/
SHA256=d163e41c56197425405e836222721ace8def3f120689fe352725fe5e3ba1a69d

user=prometheus
group=prometheus
home=/etc/prometheus
db_dir=/var/lib/prometheus
config_dir=/etc/prometheus
config=prometheus.yaml
rules_file=system.rules.yml

exporters:
	

download:
	cd $(download_path) \
	&& curl -LO $(URL)/v$(version)/$(package) \
	&& echo "$(SHA256) $(package)" | sha256sum -c - \
	&& tar -xvf $(package)  

create-user:
	groupadd $(group)
	adduser --home $(home) --group $(group) $(user)

build:
	mkdir -p $(db_dir) $(config_dir) \
	&& cd $(download_path)/$(artifacts) \
	&& cp prometeus /usr/local/bin \
	&& cp promtool /usr/local/bin \
	&& cp consoles $(home) \
	&& cp console_libraries $(home) \
	&& chown $(user):$(group) /usr/local/bin $(db_dir) $(config_dir) \
	&& chmod +x /usr/local/bin/(prometheus, promtool)

config:
	cp ./$(config) $(config_dir)/$(config) \
	&& chown $(user):$(group) $(config_dir)/$(config) \
	&& cp ./prometheus.service /etc/systemd/system/prometheus.service

validate:
	promtool check rules $(config_dir)/rules/$(rules_file)

launch:
	systemctl daemon-reload \ 
	&& systemctl enable prometheus \ 
	&& systemctl start prometheus \ 
	&& systemctl status prometheus \

clean:
	cd $(download_path) \
	&& rm -vrf $(package) $(artifacts)

remove:
	rm -vrf $(db_dir) $(config_dir) /usr/local/bin/promtool /usr/local/bin/prometeus $(home)/consoles $(home)/console_libraries \
	&& deluser --remove-home $(user) \
	&& groupdel $(group)

install: dependencies download create-user build config validate launch clean