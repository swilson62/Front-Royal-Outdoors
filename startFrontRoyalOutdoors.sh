#!/usr/bin/env bash

python3 manage.py migrate
python3 manage.py createsuperuser --noinput --username admin --email anonymous@example.com
python3 manage.py runscript populate
python3 manage.py runserver 0.0.0.0:8000
