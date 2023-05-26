FROM node:19.9.0 as npm-base

ENV LC_ALL=C.UTF-8 \
  LANG=C.UTF-8 \
  TZ=Europe/Rome

RUN mkdir code

WORKDIR /code

ENV HOST 0.0.0.0

RUN \
  apt-get -y upgrade && \
  apt -y clean && \
  apt-get -y update

RUN rm -rf node_modules

COPY . .
