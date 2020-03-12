# image name & maintainer name
FROM python:3.7-alpine
MAINTAINER Mahmoud Lebda

# stop python buffer recommend to run in container
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# make directory to copy our app source code
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create user the will run our application
RUN adduser -D user
USER user
