#!/bin/bash

cd backend/
pip3 install -r requirements.txt

sleep 2s

python3 manage.py makemigrations
python3 manage.py migrate auth
python3 manage.py migrate
# python3 manage.py collectstatic

python3 manage.py runserver 0.0.0.0:9001

