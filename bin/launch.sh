#!/bin/bash

set -e

echo "${0}: Applying migrations..."
pdm run manage.py migrate --noinput

echo "${0}: Running Gunicorn server..."
pdm run gunicorn --bind :8000 --workers 1 syntheses.wsgi
