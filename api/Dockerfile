FROM python:2-onbuild
MAINTAINER Edouard Oger edouard.oger@gmail.com

EXPOSE 5000

RUN apt-get update && apt-get install libgeos-dev -y && apt-get clean

CMD [ "./bin/server.sh" ]
