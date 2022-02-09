#!/bin/bash

python environmentsetup.py

gunicorn --bind 0.0.0.0:8800 --chdir /flask/ wsgi:app
