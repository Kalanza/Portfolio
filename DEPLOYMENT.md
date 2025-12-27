# PythonAnywhere Deployment Guide

## Prerequisites
1. Create a PythonAnywhere account at https://www.pythonanywhere.com
2. Note your username (e.g., `yourusername`)

## Step 1: Clone Repository on PythonAnywhere

Open a **Bash console** from PythonAnywhere dashboard:

```bash
git clone https://github.com/Kalanza/Portfolio.git
cd Portfolio
```

## Step 2: Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 portfolio-venv
pip install -r requirements.txt
```

## Step 3: Configure Environment Variables

```bash
cp .env.example .env
nano .env
```

Update the `.env` file with:
```
SECRET_KEY=your-new-secret-key-generate-using-django
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
```

Generate a new SECRET_KEY:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## Step 4: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

## Step 5: Run Migrations

```bash
python manage.py migrate
```

## Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

## Step 7: Populate Data

```bash
python manage.py populate_projects
python manage.py populate_experience
```

## Step 8: Configure Web App

1. Go to **Web** tab in PythonAnywhere dashboard
2. Click **Add a new web app**
3. Choose **Manual configuration** (not Django wizard)
4. Select **Python 3.10**

## Step 9: Configure WSGI File

Click on the WSGI configuration file link and replace content with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/Portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

# Load .env file
from dotenv import load_dotenv
project_folder = os.path.expanduser(path)
load_dotenv(os.path.join(project_folder, '.env'))

# Initialize Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important**: Replace `yourusername` with your actual PythonAnywhere username!

## Step 10: Configure Virtual Environment

In the **Web** tab:
- Find "Virtualenv" section
- Enter: `/home/yourusername/.virtualenvs/portfolio-venv`

## Step 11: Configure Static Files

In the **Web** tab, add static files mapping:

| URL          | Directory                                    |
|--------------|----------------------------------------------|
| /static/     | /home/yourusername/Portfolio/staticfiles     |
| /media/      | /home/yourusername/Portfolio/media           |

## Step 12: Reload Web App

Click the green **Reload** button at the top of the Web tab.

## Step 13: Visit Your Site

Your portfolio will be live at: `https://yourusername.pythonanywhere.com`

## Updating Your Site

When you make changes:

```bash
cd ~/Portfolio
git pull origin main
pip install -r requirements.txt  # if requirements changed
python manage.py migrate  # if models changed
python manage.py collectstatic --noinput
# Click Reload button in Web tab
```

## Troubleshooting

### Check Error Logs
- Go to **Web** tab
- Click on error log link
- Check server log link

### Common Issues

1. **500 Error**: Check error log, often due to:
   - Wrong SECRET_KEY or DEBUG setting
   - ALLOWED_HOSTS not configured
   - Missing dependencies

2. **Static files not loading**:
   - Verify static files mapping in Web tab
   - Run `collectstatic` again
   - Check STATIC_ROOT path

3. **Database errors**:
   - Run migrations: `python manage.py migrate`
   - Check file permissions

## Free Account Limitations

- Custom domain not available (use yourusername.pythonanywhere.com)
- One web app only
- App goes to sleep after 3 months of inactivity
- Limited CPU time

## Upgrade for Production

For a production site, consider upgrading to:
- Hacker plan ($5/month) for custom domain
- Web Developer plan for more apps and CPU time

---

**Your Portfolio is Ready! 🎉**
