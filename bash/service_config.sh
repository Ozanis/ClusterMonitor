#!/usr/bin/env bash



cat > /etc/systemd/system/DFservice << EOF
[Unit]
Description=DFservice
After=Systemd-tmpfiles-setup.service
After=Swapfile.swap

[Service]
Type=forking
PIDFile=/var/run/DFservice/DFservice.pid
WorkingDirectory=/etc/DFservice
User=${USER}
Group=
Environment=RACK-ENV=production
OOMScoreAdjust=-500
ExecStart=/usr/local/bin/bundle exec srvice -C /
ExecStop=/usr/local/bin/bundle exec srvice -S /
ExecReload=/usr/local/bin/bundle exec srvice -S /
Restart=always
TimeoutSec=60

[Install]
WantedBy=multi-user.target
EOF

systemctl enable DFservice
systemctl start DFservice

reboot