# velov-companion-server


## Dependencies

- docker
- docker-compose

## Get it running

1. Paste your JCDecaux developer API Key in a file named `apikey` at the base of the project.

2. Execute `docker-compose up` in the root folder.

## Manage the database

```
docker run -it --link velovcompanionserver_db_1:postgres --rm postgres \
    sh -c 'exec psql \velov-companion -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'
```
