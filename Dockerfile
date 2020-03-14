# image name & maintainer name
# new one 3.8-alpine
FROM python:3.7-alpine
LABEL maintainer="Mahmoud Lebda"

# stop python buffer recommend to run in container
ENV PYTHONUNBUFFERED 1


# install dependencies
COPY ./requirements.txt /requirements.txt
# dependencies for psycopg2 to work
# it uses the package manager that comes with alpine
# apk the package manager
# add for add a package
# update the registry before we add
# no cache don't store the registry index in docker
# no cache to minimize the number of extra files and packages
RUN apk add --update --no-cache postgresql-client
# temporary packages  to make requirements run in Alpine
# virtual set alias for dependancies to easly remove them
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
# install python dependencies
RUN pip install -r /requirements.txt
# remove temprary
RUN apk del .tmp-build-deps

# make directory to copy our app source code
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create user the will run our application
RUN adduser -D user
USER user
