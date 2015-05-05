# velov-companion-server


## Dependencies

- docker
- docker-compose

## Get it running

1. Create a configuration file named `conf.env` based on `conf.env.template`.

2. Execute `docker-compose up` in the root folder.

## DB Admin

`docker run -t -i --link velovcompanionserver_db_1:db eoger/postgis psql velov_companion -h db -U velov_companion`

## Boot2Docker

If you're using boot2docker and can't connect to the server, try adding a port redirection to Virtualbox:
`VBoxManage controlvm boot2docker-vm natpf1 "guest-velov-flask,tcp,,8080,,8080"`