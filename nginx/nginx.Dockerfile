FROM debian:buster

RUN apt-get update && apt-get install -y nginx \
                                         nano \
    && rm -rf /var/lib/apt/lists/*

COPY ./nginx/ /etc/nginx/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]