FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev libffi-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    py3-pip python3-dev pango jpeg-dev openjpeg-dev g++
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt