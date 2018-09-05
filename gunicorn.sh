#! /bin/bash


gunicorn -t99999 --workers 1 --reload --bind :8081 wsgi:app

