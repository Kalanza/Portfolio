# +++++++++++ DJANGO +++++++++++
# To use your own Django app, modify the following:
# 1. Replace 'YourUsername' with your PythonAnywhere username
# 2. Replace '/home/YourUsername/Portfolio' with the actual path to your project

import os
import sys

# Add your project directory to the sys.path
path = '/home/YourUsername/Portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_site.settings'

# Set DEBUG to False for production
os.environ.setdefault('DEBUG', 'False')

# Activate your virtual environment
# virtualenv = '/home/YourUsername/.virtualenvs/portfolio-venv/bin/activate_this.py'
# with open(virtualenv) as f:
#     exec(f.read(), {'__file__': virtualenv})

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
