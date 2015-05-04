FROM python:2-onbuild
MAINTAINER Edouard Oger edouard.oger@gmail.com

EXPOSE 5000

RUN apt-get update && apt-get install -y \
    libgeos-dev

CMD [ "./bin/server.sh" ]
