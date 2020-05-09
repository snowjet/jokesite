#!/usr/bin/bash

if [ -z ${POSTGRESQL_SERVICE_HOST} ] ; then
    export DJANGO_SETTINGS_MODULE=jokesite.devsettings
    gunicorn jokesite.wsgi:application --bind 0.0.0.0:8080
else
    export DJANGO_SETTINGS_MODULE=jokesite.settings
    gunicorn jokesite.wsgi:application --bind 0.0.0.0:8080
fi