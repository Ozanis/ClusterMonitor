#!/usr/bin/env bash


mkdir /usr/bin/DF/DF.srvice

mv DF.service /usr/bin/DF/DF.srvice

systemctl daemon-reload

systemctl start df.service         #To start running service
