# velov-companion-server


## Dependencies

- docker
- docker-compose

## Get it running

1. Create a configuration file named `conf.env` based on `conf.env.template`.

2. Execute `docker-compose up` in the root folder.

## DB Admin

`docker run -t -i --link velovcompanionserver_db_1:db eoger/postgis psql velov_companion -h db -U velov_companion`