# This is a multi-stage build file, which means a stage is used to build
# the backend (dependencies), the frontend stack and a final production
# stage re-using assets from the build stages. This keeps the final production
# image minimal in size.

# Stage 1 - Backend build environment
# includes compilers and build tooling to create the environment

FROM python:3.8 AS backend-build

RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Ensure we use the latest version of pip
RUN pip install pip setuptools -U
COPY ./requirements /app/requirements
RUN pip install -r requirements/production.txt


# Stage 2 - Install frontend deps and build assets
FROM mhart/alpine-node:10 AS frontend-build

RUN apk --no-cache add \
    git

WORKDIR /app

# copy configuration/build files
COPY ./*.json /app/
COPY ./*.js /app/
COPY ./build /app/build/

# install WITH dev tooling
RUN npm ci

# copy source code
COPY ./src /app/src

# build frontend
RUN npm run build


# Stage 3 - Build docker image suitable for production
FROM python:3.8 AS production

RUN apt-get update && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ./bin/docker_start.sh /start.sh
RUN mkdir /app/log

# copy backend build deps
COPY --from=backend-build /usr/local/lib/python3.8 /usr/local/lib/python3.8
COPY --from=backend-build /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# copy build statics
COPY --from=frontend-build /app/node_modules/font-awesome /app/node_modules/font-awesome
COPY --from=frontend-build /app/src/beheerconsole/static /app/src/beheerconsole/static

# copy source code
COPY ./src /app/src
RUN mkdir /app/media

ENV DJANGO_SETTINGS_MODULE=beheerconsole.conf.docker

ARG SECRET_KEY=dummy

# Run collectstatic, so the result is already included in the image
RUN python src/manage.py collectstatic --noinput

EXPOSE 8000
CMD ["/start.sh"]
