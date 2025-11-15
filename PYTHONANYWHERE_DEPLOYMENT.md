# PythonAnywhere Deployment Guide

## Step 1: Create PythonAnywhere Account
1. Go to https://www.pythonanywhere.com/
2. Sign up for a free Beginner account
3. Verify your email

## Step 2: Upload Your Code

### Option A: Using Git (Recommended)
1. Open a **Bash console** from your PythonAnywhere dashboard
2. Clone your repository:
```bash
git clone https://github.com/Kalanza/Portfolio.git
cd Portfolio
```

### Option B: Upload Files
1. Go to **Files** tab
2. Upload your project files manually

## Step 3: Set Up Virtual Environment
In the Bash console:
```bash
cd ~/Portfolio
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 4: Configure Static Files
```bash
python manage.py collectstatic --noinput
```

## Step 5: Set Up Database
```bash
python manage.py migrate
python manage.py populate_data
```

## Step 6: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## Step 7: Configure Web App
1. Go to **Web** tab → **Add a new web app**
2. Choose **Manual configuration**
3. Select **Python 3.10**
4. Click **Next**

### Configure WSGI file:
1. In the Web tab, click on the **WSGI configuration file** link
2. Delete all existing content
3. Copy and paste the content from `.pythonanywhere_wsgi.py`
4. Replace `YourUsername` with your actual PythonAnywhere username (appears in the path at top)
5. Save the file

### Configure Virtual Environment:
1. In the Web tab, find **Virtualenv** section
2. Enter: `/home/YourUsername/.virtualenvs/portfolio-venv` or `/home/YourUsername/Portfolio/venv`
3. Click the checkmark

### Configure Static Files:
1. In the Web tab, find **Static files** section
2. Add:
   - URL: `/static/`
   - Directory: `/home/YourUsername/Portfolio/staticfiles`
3. Add:
   - URL: `/media/`
   - Directory: `/home/YourUsername/Portfolio/media`

## Step 8: Set Environment Variables
1. In the Web tab, scroll down to **Environment variables**
2. Add:
   - Name: `SECRET_KEY`, Value: `django-insecure-3pzkv(**5z14nrmvmg4i!216wri)$jh2rrup0&1o0$j2lw$hn7` (or generate a new one)
   - Name: `DEBUG`, Value: `False`
   - Name: `ALLOWED_HOSTS`, Value: `yourusername.pythonanywhere.com`

## Step 9: Reload Web App
1. In the Web tab, click the green **Reload** button
2. Visit your site at: `https://yourusername.pythonanywhere.com`

## Troubleshooting

### Check Error Logs
- In the Web tab, check:
  - **Error log** (bottom of page)
  - **Server log** (bottom of page)

### Common Issues

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```
Then reload the web app.

**Database errors:**
```bash
python manage.py migrate
python manage.py populate_data
```

**Import errors:**
Make sure virtual environment is activated and all packages installed:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Update Your Site
When you make changes:
```bash
cd ~/Portfolio
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```
Then reload the web app from the Web tab.

## Free Account Limitations
- 1 web app only
- Limited CPU seconds per day
- Site accessible at `yourusername.pythonanywhere.com`
- SQLite database (no PostgreSQL on free tier)
- Must visit site every 3 months or account expires

## Custom Domain (Paid Only)
To use `victorkalanza.com`, you need a paid PythonAnywhere account.
