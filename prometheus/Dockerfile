FROM alpine:3.13.2
ENV URL="https://dl.grafana.com/oss/release" \
    VERSION="7.4.3" \
    PACKAGE="prometheus-${VERSION}.linux-amd64.tar.gz" \
    SHA256="d163e41c56197425405e836222721ace8def3f120689fe352725fe5e3ba1a69d" \
    HOME="/etc/prometheus" \
    USER="prometheus" \
    GROUP="prometheus" \
    ARTIFACT="prometheus"
RUN groupadd ${GROUP} \
	&& adduser --home ${HOME} --group ${GROUP} ${USER} \
    \
    && apk add --no-cache curl go \
    \
    && cd /tmp/ \
	&& curl -LO "${URL}/${PACKAGE}" -O "${ARTIFACT}.tar.gz" \
	&& echo "${SHA256} ${ARTIFACT}.tar.gz" | sha256sum -c - \
	&& tar -xvf "${ARTIFACT}" \
    \
    && cd 
	&& mkdir -p /var/lib/prometheus ${HOME} \
	&& cd /tmp/${ARTIFACTS} \
	&& cp prometeus /usr/local/bin \
	&& cp promtool /usr/local/bin \
	&& cp consoles ${HOME} \
	&& cp console_libraries ${HOME} \
	&& chown ${USER}:${GROUP} /usr/local/bin /var/lib/prometheus ${HOME} \
	&& chmod +x /usr/local/bin/prometheus /usr/local/bin/promtool \
    \
    && rm -vrf ${ARTIFACT} ${PACKAGE}

COPY --chown="${USER}:${GROUP}" ./prometheus/prometheus.yml /etc/prometheus/prometheus.yml
COPY --chown="${USER}:${GROUP}" ./prometheus/rules/ /etc/prometheus/rules/
COPY --chown="${USER}:${GROUP}" ./prometheus/alerts/ /etc/prometheus/rules/alerts/
COPY --chown="${USER}:${GROUP}" ./prometheus/alertmanager/ /etc/prometheus/rules/alertmanager/

ENTRYPOINT [ "" ]