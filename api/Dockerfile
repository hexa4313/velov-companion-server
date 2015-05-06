FROM nginx

RUN mkdir -p /home/docker/code/app/
WORKDIR /home/docker/code/

RUN \
  apt-get update && apt-get install -y --no-install-recommends \
    python-software-properties \
    python-setuptools \
    build-essential \
    supervisor \
    python-dev \
    libpq-dev \
    python \
    git \
    libgeos-dev
RUN easy_install pip
RUN pip install uwsgi
RUN mkdir -p /var/log/supervisor
RUN rm /etc/nginx/conf.d/default.conf

COPY app/requirements.txt /home/docker/code/app/
RUN pip install -r app/requirements.txt

COPY nginx.conf /etc/nginx/nginx.conf

COPY . /home/docker/code/

EXPOSE 80

CMD ./bin/server.sh
