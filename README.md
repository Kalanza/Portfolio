# Django Portfolio Website

A modern, beautiful portfolio website built with Django framework, featuring a dark gradient theme with purple and cyan accents.

## Features

- **Dynamic Content Management**: Add and manage your profile, skills, and projects through Django Admin
- **Beautiful Design**: Modern dark theme with gradient backgrounds and smooth animations
- **Responsive Layout**: Fully responsive design that works on all devices
- **Easy Customization**: Simple model structure for quick content updates

## Tech Stack

- **Backend**: Django 5.2+
- **Database**: SQLite (easily switchable to PostgreSQL)
- **Frontend**: HTML5, CSS3 (Inter font from Google Fonts)
- **Design**: Custom CSS based on Figma design specifications

## Project Structure

```
Portfolio/
├── portfolio/                  # Main app
│   ├── models.py              # Database models (Profile, Skill, Project, Technology)
│   ├── views.py               # View logic
│   ├── admin.py               # Admin panel configuration
│   ├── urls.py                # App URL routing
│   ├── templates/             # HTML templates
│   │   └── portfolio/
│   │       └── index.html     # Main portfolio page
│   ├── static/                # Static files
│   │   └── portfolio/
│   │       ├── css/
│   │       │   └── style.css  # Main stylesheet
│   │       └── images/        # Image assets
│   └── management/            # Custom management commands
│       └── commands/
│           └── populate_data.py  # Sample data seeder
├── portfolio_site/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install django pillow
```

### Step 2: Run Migrations

The migrations have already been created and applied. If you need to reset the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 4: Populate Sample Data (Optional)

```bash
python manage.py populate_data
```

This will create:
- A sample profile (Haneef Ojutalayo)
- 15 technical skills
- 4 featured projects with technologies

### Step 5: Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your portfolio!

Visit `http://127.0.0.1:8000/admin/` to manage content.

## Customization Guide

### Update Your Profile

1. Log in to the admin panel at `http://127.0.0.1:8000/admin/`
2. Navigate to **Portfolio > Profiles**
3. Edit the existing profile or create a new one
4. Update your:
   - Name
   - Title
   - Bio
   - Email & Phone
   - Social media links (GitHub, LinkedIn)
   - Profile image

### Add/Edit Skills

1. Go to **Portfolio > Skills**
2. Add new skills or edit existing ones
3. Use the "order" field to control the display sequence

### Add/Edit Projects

1. Go to **Portfolio > Projects**
2. Create or edit projects with:
   - Title
   - Stage (0-3)
   - Description
   - Order (for sorting)
3. Add technologies to each project inline

### Customize Styling

Edit `portfolio/static/portfolio/css/style.css` to modify:
- Colors and gradients
- Fonts and typography
- Layout and spacing
- Responsive breakpoints

## Models Overview

### Profile
- Stores your personal information
- Only one profile should exist (managed as singleton)

### Skill
- Technical skills displayed as badges
- `order` field controls display sequence

### Project
- Featured projects with stage indicators (0-3)
- Related to technologies via foreign key

### Technology
- Technologies used in each project
- Displayed as small badges on project cards

## Deployment Tips

### For Production:

1. **Update settings.py**:
   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com']
   ```

2. **Use a production database** (PostgreSQL recommended):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'portfolio_db',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

4. **Use a production server** like Gunicorn or uWSGI

## Color Palette

- **Background**: Linear gradient from #0F172B to #1D293D
- **Primary Accent**: #C27AFF (Purple)
- **Secondary Accent**: #00D3F2 (Cyan)
- **Text Primary**: #F1F5F9 (White)
- **Text Secondary**: #CAD5E2 (Light Gray)
- **Text Muted**: #90A1B9 (Gray)
- **Border/Divider**: #314158 (Dark Blue)

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

This project is open source and available for personal and commercial use.

## Support

For issues or questions, please create an issue in the repository.

---

Built with ❤️ using Django
