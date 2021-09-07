# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./app/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

# copy project
# COPY ./app /app
