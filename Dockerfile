FROM python:3.11.2-alpine


WORKDIR /1cgss_sync_python

ARG BUILD_DEPS="build-base gcc libffi-dev openssl-dev libpq-dev"
ARG RUNTIME_DEPS="libcrypto1.1 libssl1.1 libpq-dev"

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps ${BUILD_DEPS} \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps \
    && apk add --no-cache ${RUNTIME_DEPS}

COPY . /1cgss_sync_python
