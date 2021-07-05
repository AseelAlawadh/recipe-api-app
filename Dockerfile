FROM python:3.7-alpine
MAINTAINER Aseel

#run unbuffered mode recommended when running Python docker containers to avoid some complications when running docker image
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


#make a directory within Docker image that can use to store the app

#create a empty folder
RUN mkdir /app
WORKDIR /app
COPY ./app  /app

#create user that is going to runnig just the app
RUN adduser -D user
#switch docjkeruser(root) to created user
USER user
