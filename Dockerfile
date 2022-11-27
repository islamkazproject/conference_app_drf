FROM python:3.11-alpine
MAINTAINER Conference

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apt-get update\
    &&apt-get upgrade pip\
    &&pip install --upgrade pip\
    &&pip lock -r > requirements.txt\
    &&pip install -r /requirements.

RUN mkdir /conference
WORKDIR /conference
COPY ./conference /conference

RUN adduser -D user
USER user