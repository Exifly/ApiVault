#!/bin/bash

cd /code/

pip3 install -r requirements.txt

sleep 2s

# python3 manage.py collectstatic

python3 start.py

