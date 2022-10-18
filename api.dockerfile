FROM python:3.10.8-alpine3.16
LABEL author="Cauã Bernardino"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev python3-dev \
    musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
# Delete tmp
RUN apk del .tmp-build-deps

RUN mkdir /api
WORKDIR /api
COPY ./api /api

RUN adduser -D runner
USER runner