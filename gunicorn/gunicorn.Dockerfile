FROM debian:buster

RUN apt-get update && apt-get install -y python3 \
                                         python3-pip \
                                         nano \
                                         libmariadb-dev \
                                         libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install django djangorestframework mysqlclient gunicorn psycopg2-binary
WORKDIR /var/www/html/rest/

CMD ["gunicorn", "-c gunicorn.conf.py", "rest.wsgi"]