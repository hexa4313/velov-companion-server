#!/bin/bash

function check_up() {
    service=$1
    host=$2
    port=$3

    max=13 # 1 minute

    counter=1
    while true;do
        python -c "import socket;s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.connect(('$host', $port))" \
        >/dev/null 2>/dev/null && break || \
        echo "Waiting that $service on ${host}:${port} is started (sleeping for 5)"

        if [[ ${counter} == ${max} ]];then
            echo "Could not connect to ${service} after some time"
            echo "Investigate locally the logs with fig logs"
            exit 1
        fi

        sleep 5

        (( counter++ ))
    done
}

# Wait until the DB Server is ready
sleep 5
check_up "DB Server" ${DB_PORT_5432_TCP_ADDR} 5432

# Launch the jobs runner
/usr/bin/supervisord -c /home/docker/code/supervisord.conf