#!/bin/bash
# Build script for DigitalOcean App Platform

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate --no-input
