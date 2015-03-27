FROM python:3.5-alpine

WORKDIR /app

ADD . /app

RUN apk update && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        postgresql-dev \
    && pip install -r requirements.txt \
    && apk del .build-deps

RUN apk update && apk add \
    redis

EXPOSE 8000

WORKDIR /app/application

ENV DJANGO_SETTINGS_MODULE=config.settings.dev \
    PYTHONUNBUFFERED=0

CMD ["python", "manage.py", "runserver", "0:8000"]

