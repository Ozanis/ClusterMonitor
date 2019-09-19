#!/usr/bin/env bash

packs=("openssl", "python-pip", "python-pyopenssl", "ufw", "sqlite3")

check_pack(pack){
	if [[-z "`dpkg -l ${pack}`"]] then
		eval "apt install ${pack}"
	fi
}

for i in ${packs}do
	check_pack(i)
done

pip install psutil

mkdir /usr/bin/DF/DF.srvice
mv DF.service /usr/bin/DF/DF.srvice
systemctl daemon-reload
systemctl start df.service         
