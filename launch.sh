#!/bin/bash

CID=$(sudo docker run -d -v ~/velov-companion-server:/src eoger/flask-restful /sbin/my_init)
echo -n "Flask container IP : "
sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' $CID
