FROM node:onbuild

VOLUME ["/usr/src/app/segments"]

RUN apt-get update && apt-get install -y default-jre
RUN cd segments && curl http://brouter.de/brouter/segments3/E0_N45.rd5 -o E0_N45.rd5

EXPOSE 8888