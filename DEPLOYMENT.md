# PythonAnywhere Deployment Guide

Dr. Michelle Echeverry - Patient Payment Tracker

## Prerequisites

- PythonAnywhere account (free or paid)
- GitHub repository with the code
- Custom domain (optional)

## Step-by-Step Deployment

### 1. Create Web App on PythonAnywhere

1. Log in to your PythonAnywhere dashboard
2. Go to **Web** tab
3. Click **Add a new web app**
4. Choose **Manual configuration**
5. Select **Python 3.10** (or later)
6. Click **Create**

### 2. Clone the Repository

In PythonAnywhere Bash console:

```bash
cd /home/your-username
git clone https://github.com/your-username/Mich_Proy.git
cd Mich_Proy
```

### 3. Create and Activate Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 mich_proy
pip install -r requirements.txt
```

### 4. Configure Web App

1. In the **Web** tab, find your app and click on it
2. In the **Virtualenv** section, enter the path:
   ```
   /home/your-username/.virtualenvs/mich_proy
   ```

3. In the **Code** section:
   - **Source code**: `/home/your-username/Mich_Proy`
   - **Working directory**: `/home/your-username/Mich_Proy`

### 5. Update WSGI Configuration

1. Click on the WSGI configuration file link
2. Replace the content with:

```python
import os
import sys

# Add your project to the path
path = '/home/your-username/Mich_Proy'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'doctor_payments.settings'
os.environ['DEBUG'] = 'False'
os.environ['ALLOWED_HOSTS'] = 'your-domain.pythonanywhere.com'
os.environ['DJANGO_SECRET_KEY'] = 'generate-a-secure-key-here'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 6. Generate Secure Secret Key

In the PythonAnywhere Bash console:

```bash
python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and set it in your WSGI configuration.

### 7. Configure Static Files

In the **Web** tab, under **Static files**:

1. Add a new static file mapping:
   - URL: `/static/`
   - Directory: `/home/your-username/Mich_Proy/staticfiles`

2. In the Bash console:

```bash
cd /home/your-username/Mich_Proy
python manage.py collectstatic --noinput
```

### 8. Initialize Database

In the Bash console:

```bash
cd /home/your-username/Mich_Proy
python manage.py migrate
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

### 9. Reload the Web App

In the **Web** tab, click the green **Reload** button to apply all changes.

### 10. Access Your Application

Your app is now available at:
- Main site: `https://your-username.pythonanywhere.com`
- Admin panel: `https://your-username.pythonanywhere.com/admin`

## Custom Domain Setup (Optional)

1. In PythonAnywhere **Web** tab, under **Web app name**, update to your custom domain
2. Configure your domain provider's DNS settings to point to PythonAnywhere
3. Set up an SSL certificate in the **Security** section

## Environment Variables

Important environment variables to set in your WSGI file:

- `DEBUG = 'False'` - Disable debug mode in production
- `ALLOWED_HOSTS` - Your domain name
- `DJANGO_SECRET_KEY` - Generate a secure key (never commit to git)

## Backup & Maintenance

### Regular Backups

```bash
# Backup database
cp /home/your-username/Mich_Proy/db.sqlite3 /home/your-username/backups/db_$(date +%Y%m%d).sqlite3
```

### Update Application

```bash
cd /home/your-username/Mich_Proy
git pull origin main
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

Then reload the web app.

## Troubleshooting

### 500 Internal Server Error
- Check error logs in the **Web** tab
- Verify WSGI configuration
- Ensure static files are collected
- Check database migrations are applied

### Page not found (404)
- Verify `ALLOWED_HOSTS` in WSGI configuration
- Check URL routes in `doctor_payments/urls.py`

### Static files not loading
- Run `python manage.py collectstatic`
- Verify static files URL mapping in Web tab
- Clear browser cache

### Database issues
- Run migrations: `python manage.py migrate`
- Check file permissions on `db.sqlite3`

## Project Structure

```
Mich_Proy/
├── requirements.txt          # Python dependencies
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
├── doctor_payments/        # Django project settings
│   ├── settings.py         # Project configuration
│   ├── urls.py             # URL routing
│   ├── wsgi.py             # WSGI application
│   └── __init__.py
├── payments/               # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── forms.py            # Django forms
│   ├── urls.py             # App URL patterns
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   └── __init__.py
└── venv/                   # Virtual environment (not deployed)
```

## Security Checklist

- ✓ DEBUG is False in production
- ✓ SECRET_KEY is a random, secure string
- ✓ ALLOWED_HOSTS is configured correctly
- ✓ SSL/HTTPS is enabled
- ✓ Static files are properly configured
- ✓ Database is backed up regularly
- ✓ Environment variables are not committed to git

## Support

For PythonAnywhere-specific issues, visit: https://www.pythonanywhere.com/help/

For Django documentation: https://docs.djangoproject.com/
