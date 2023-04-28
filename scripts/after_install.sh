#!/usr/bin/env bash




# Kill any servers that may be running in the background

sudo pkill -f runserver




# Kill frontend servers if you are deploying any frontend

sudo pkill -f tailwind

sudo pkill -f node

cd /home/ec2-user/django-aws_cicd/




# Activate virtual environment

python3 -m venv venv

source venv/bin/activate




# Install requirements.txt

pip install -r /home/ec2-user/django-aws_cicd/requirements.txt




# Run server

screen -d -m python3 manage.py runserver 0:8000