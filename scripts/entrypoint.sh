#!/bin/sh

# this is to exit the script if there is any error with the script with a exit code 0. This useful for debugging issues
set -e

# this is a command to collect all static files and put them in a static folder
python manage.py collectstatic --noinput

#Command that runs our django application in uwsgi
uwsgi --socket :8000 --master --enable-threads --module AkantBook.wsgi