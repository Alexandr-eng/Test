
FROM python:3.11.9

WORKDIR app/usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt app/usr/app/

RUN pip install -r requirements.txt

COPY . app/usr/app/