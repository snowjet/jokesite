#!/usr/bin/bash

if [ -z ${DATABASE_SERVICE_NAME} ] ; then
    export DJANGO_SETTINGS_MODULE=jokesite.devsettings
    echo "Using development settings"
else
    export DJANGO_SETTINGS_MODULE=jokesite.settings
    echo "Using Postgres: ${DATABASE_SERVICE_NAME}"
fi
gunicorn jokesite.wsgi:application --bind 0.0.0.0:8080