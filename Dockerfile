FROM python:3.8.3-alpine

ENV HOME=/usr/src/app
ENV APP_HOME=$HOME/web
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir $HOME && mkdir $APP_HOME && mkdir $APP_HOME/staticfiles

WORKDIR $APP_HOME

RUN apk update && \
    apk add zlib-dev jpeg-dev postgresql-dev gcc python3-dev musl-dev && \
    apk add --update alpine-sdk && apk add libffi-dev openssl-dev cargo rust

COPY ./requirements ./requirements

RUN pip install -U pip && \
    pip install --upgrade pip && \
    pip install pipenv && \
    pip install -r requirements/dev.txt

COPY ./docker-entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/web/docker-entrypoint.sh"]