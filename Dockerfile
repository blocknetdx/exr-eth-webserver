# Build via docker:
# docker build --build-arg cores=8 -t ethereum-webserver .
# docker run -d --name ethereum-webserver -p 80:80 ethereum-webserver:latest

FROM nginx

ARG cores=1
ENV ecores=$cores

RUN apt update \
  && apt install -y --no-install-recommends \
     software-properties-common \
     ca-certificates \
     python3 nano \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt update \
  && apt install -y --no-install-recommends \
     build-essential \
     python3-dev python3-pip python3-setuptools \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Update pip
RUN pip3 install --upgrade pip

# Make directory and set as working directory
RUN mkdir -p /opt/app
WORKDIR /opt/app

# Write nginx.conf /etc/nginx/nginx.conf
RUN echo "                                                                         \n\
user www-data;                                                                     \n\
worker_processes $ecores;                                                          \n\
pid /run/nginx.pid;                                                                \n\
events {                                                                           \n\
    worker_connections 1024;                                                       \n\
    use epoll;                                                                     \n\
    multi_accept on;                                                               \n\
}                                                                                  \n\
http {                                                                             \n\
    access_log /dev/stdout;                                                        \n\
    error_log /dev/stdout;                                                         \n\
    sendfile            on;                                                        \n\
    tcp_nopush          on;                                                        \n\
    tcp_nodelay         on;                                                        \n\
    keepalive_timeout   65;                                                        \n\
    types_hash_max_size 2048;                                                      \n\
    include             /etc/nginx/mime.types;                                     \n\
    default_type        application/octet-stream;                                  \n\
    index   index.html index.htm;                                                  \n\
    server {                                                                       \n\
        listen       80 default_server;                                            \n\
        listen       [::]:80 default_server;                                       \n\
        server_name  localhost;                                                    \n\
        root         /var/www/html;                                                \n\
        location / {                                                               \n\
            include uwsgi_params;                                                  \n\
            uwsgi_pass unix:/tmp/uwsgi.socket;                                     \n\
        }                                                                          \n\
    }                                                                              \n\
}                                                                                  \n\
                                                                                   \n\
\n" > /etc/nginx/nginx.conf

# Write uwsgi.ini /opt/app/uwsgi.ini
RUN echo "                                                                                                         \n\
[uwsgi]                                                                                                            \n\
module = ethereum:app                                                                                              \n\
uid = www-data                                                                                                     \n\
gid = www-data                                                                                                     \n\
master = true                                                                                                      \n\
processes = $ecores                                                                                                \n\
                                                                                                                   \n\
socket = /tmp/uwsgi.socket                                                                                         \n\
chmod-sock = 664                                                                                                   \n\
vacuum = true                                                                                                      \n\
                                                                                                                   \n\
die-on-term = true                                                                                                 \n\
                                                                                                                   \n\
\n" > /opt/app/uwsgi.ini

# Install app dependencies from requirements.txt
COPY requirements.txt /opt/app
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy startup script
COPY start.sh /opt/app

# Bundle Python app source
COPY ethereum.py /opt/app

# Expose port 80
EXPOSE 80

# Execution rights and set default command
RUN chmod +x ./start.sh
CMD ["./start.sh"]
