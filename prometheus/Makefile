OS=$(cat /etc/*release | grep DISTRIB_ID | cut -d"=" -f 2)
deps="tar curl golang"

download_path=/tmp
artifacts=prometheus_files
URL=https://prometheus.io/download
package=prometheus-2.25.0.linux-amd64.tar.gz
SHA256=d163e41c56197425405e836222721ace8def3f120689fe352725fe5e3ba1a69d

user=prometheus
group=prometheus
home=/etc/prometheus
db_dir=/var/lib/prometheus
config_dir=/etc/prometheus
config=prometheus.yaml
rules_file=system.rules.yml

dependencies:
	apt-get update \
	&& apt-get upgrade \
	&& apt-get install $(deps) -y 

download:
	curl $(URL)/$(package) -o $(download_path) | sha256sum 

unarchive:
	tar -zxvf $(download_path)/$(package) -o $(artifacts)

create-user:
	groupadd $(group)
	adduser -m -d $(home) -G $(group) $(user)


build:
	mkdir $(db_dir) $(config_dir) \
	&& cp $(download_path)/$(artifacts)/prometeus /usr/local/bin \
	&& cp $(download_path)/$(artifacts)/promtool /usr/local/bin \
	&& cp $(download_path)/$(artifacts)/consoles $(home) \
	&& cp $(download_path)/$(artifacts)/console_libraries $(home) \
	&& chown $(user):$(group) /usr/local/bin $(db_dir) $(config_dir) \

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
	rm -vrf $(download_path)/$(package) rm -vrf $(download_path)/$(artifacts)

remove:
	rm -vrf $(db_dir) $(config_dir) /usr/local/bin/promtool /usr/local/bin/prometeus $(home)/consoles $(home)/console_libraries 

install:
	dependencies download unarchive create-user build config validate launch clean
