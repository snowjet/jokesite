#!/usr/bin/bash

if [ -z ${POSTGRESQL_SERVICE_HOST} ] ; then
    export DJANGO_SETTINGS_MODULE=jokesite.devsettings
    echo "Using development settings"
else
    export DJANGO_SETTINGS_MODULE=jokesite.settings
    echo "Using Postgres: ${POSTGRESQL_SERVICE_HOST}"
fi
gunicorn jokesite.wsgi:application --bind 0.0.0.0:8080