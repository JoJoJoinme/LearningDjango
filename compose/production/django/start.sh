#!/bin/sh

python managy.py migrate
python managy.py collectstatic --noinput
gunicorn PersonalBlog.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/app