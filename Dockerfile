FROM python:2.7

WORKDIR /app

RUN apt-get update && apt-get install -yy libgeos-dev
ADD requirements.txt /app/

RUN pip install -U pip wheel uwsgi && pip install -r requirements.txt

#copy all files
ADD . /app
COPY docker/ /app/

EXPOSE 3031

RUN mkdir /log && apt-get install -yy redis-server

CMD /app/docker_start.sh
