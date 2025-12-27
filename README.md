# Portfolio Website

A modern, responsive portfolio website for a Senior Backend Developer built with Django.

## Features

- **Split-screen hero section** with asymmetric layout
- **Responsive design** that works on all devices
- **Project showcase** emphasizing tech stack, database schemas, and API documentation
- **Experience timeline** highlighting backend development work
- **Services section** showcasing backend expertise
- **Django admin** for easy content management

## Tech Stack

- **Framework:** Django 4.2
- **Styling:** Tailwind CSS (CDN)
- **Database:** SQLite (development) / PostgreSQL (production)
- **Python:** 3.8+

## Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Portfolio
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment
**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create a superuser (for admin access)
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the website.

## Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` to manage:
- Projects
- Services
- Experience entries

## Customization

### Update Personal Information

1. **Name and Title**: Edit [templates/portfolio/home.html](templates/portfolio/home.html) - search for "VICTOR MUMO" and the headline text
2. **About Section**: Update the content in the About section of [templates/portfolio/home.html](templates/portfolio/home.html)
3. **Contact Info**: Update email and LinkedIn links in the Contact section

### Add Your Photo

1. Replace the placeholder in the hero section (right column)
2. For best results, use a PNG with transparent background
3. Update the image section in [templates/portfolio/home.html](templates/portfolio/home.html)

### Color Scheme

The color palette is defined in [templates/base.html](templates/base.html):
- **Primary Dark:** `#111827` (Navy/Black)
- **Primary Light:** `#D8C3A5` (Beige/Gold)

### Add Content via Admin

1. Log in to the admin panel
2. Add **Projects** with:
   - Title and description
   - Tech stack
   - Database schema details
   - API documentation links
   - GitHub repository links
3. Add **Services** you offer
4. Add **Experience** entries with job details

## Deployment

### For Production

1. Update `SECRET_KEY` in [portfolio_project/settings.py](portfolio_project/settings.py)
2. Set `DEBUG = False`
3. Add your domain to `ALLOWED_HOSTS`
4. Configure PostgreSQL database
5. Set up static files collection:
   ```bash
   python manage.py collectstatic
   ```
6. Deploy to your hosting platform (AWS, Heroku, DigitalOcean, etc.)

## Project Structure

```
Portfolio/
├── manage.py
├── requirements.txt
├── portfolio_project/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/                   # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # URL routing
│   └── admin.py                # Admin configuration
└── templates/
    ├── base.html               # Base template
    └── portfolio/
        ├── home.html           # Homepage
        └── portfolio.html      # Full portfolio page
```

## Features to Add

- [ ] Contact form with email integration
- [ ] Blog section
- [ ] Testimonials
- [ ] Skills progress bars
- [ ] Dark mode toggle
- [ ] Project filtering by technology

## License

MIT License - Feel free to use this template for your own portfolio!

## Credits

Design inspired by modern editorial layouts with a focus on backend development expertise.
