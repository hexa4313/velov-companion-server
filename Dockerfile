FROM python:2-onbuild
MAINTAINER Edouard Oger edouard.oger@gmail.com

EXPOSE 5000

CMD [ "./launch.sh" ]
