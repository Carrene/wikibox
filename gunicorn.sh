#! /bin/bash


gunicorn --workers 1 --reload --bind :8081 wsgi:app

