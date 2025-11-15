#!/bin/bash
# Build script for DigitalOcean App Platform

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --no-input

# Populate initial data (only if tables are empty)
python manage.py populate_data || true

# Collect static files
python manage.py collectstatic --no-input
