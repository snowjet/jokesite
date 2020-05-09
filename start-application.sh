#!/usr/bin/bash

if [ -n POSTGRESQL_SERVICE_HOST ] ; then
    DJANGO_SETTINGS_MODULE=project.settings
    gunicorn jokesite.wsgi:application --bind 0.0.0.0:8080
else
    DJANGO_SETTINGS_MODULE=project.devsettings
    gunicorn jokesite.wsgi:application --bind 0.0.0.0:8080
fi