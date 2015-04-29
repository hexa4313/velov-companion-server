#!/bin/bash

CID=$(sudo docker run -d -v ~/velov-companion-server:/src zaha/flask /scripts/launch.sh)
echo -n "Flask container IP : "
sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' $CID
