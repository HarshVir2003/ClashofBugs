#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate

wget https://github.com/judge0/judge0/releases/download/v1.13.0/judge0-v1.13.0.zip
unzip judge0-v1.13.0.zip
cd judge0-v1.13.0
docker-compose up -d db redis
sleep 10s
docker-compose up -d
sleep 5s
