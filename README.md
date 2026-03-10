# 💙 Dr. Michelle Echeverry - Patient Payment Tracker

A professional Django web application for tracking and managing patient payment records with detailed commission calculations and monthly reporting.

## Features

✨ **Payment Management**
- Record patient payments with multiple payment methods
- Track appointment dates and patient information
- Support for Cash, Clave, Visa/MasterCard, Yappy, and Sigma insurance

📊 **Financial Analytics**
- **Totals by Payment Method** - See aggregated revenue per payment method
- **Commission Calculations** - Automatic bank commission and ITBMS (7%) calculations
  - Clave: 2% commission
  - Visa/MasterCard: 3% commission
  - Yappy: 1% commission
  - Sigma Insurance: No commission
- **Doctor Commission** - Automatic 40% calculation with separate breakdown for regular and Sigma payments

📅 **Monthly Filtering**
- Browse historical payment records by month
- All calculations dynamically update based on selected month
- Dropdown selector with available months

🌐 **Professional UI**
- Fully responsive design
- Color-coded tables (blue for income, orange for expenses)
- Clean, modern interface with gradient headers
- Spanish language interface

## Technology Stack

- **Backend**: Django 6.0.3
- **Frontend**: HTML5, CSS3
- **Database**: SQLite3
- **Server**: WSGI-compatible (PythonAnywhere ready)
- **Python**: 3.10+

## Quick Start (Local Development)

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/Mich_Proy.git
   cd Mich_Proy
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Admin Account**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run Server**
   ```bash
   python manage.py runserver
   ```

7. **Access Application**
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Project Structure

```
Mich_Proy/
├── requirements.txt              # Python dependencies
├── DEPLOYMENT.md                 # PythonAnywhere deployment guide
├── README.md                     # This file
├── .gitignore                    # Git ignore rules
├── manage.py                     # Django management script
├── db.sqlite3                    # SQLite database
│
├── doctor_payments/              # Django project configuration
│   ├── settings.py              # Django settings (env-ready)
│   ├── urls.py                  # Project URL routing
│   ├── wsgi.py                  # WSGI application
│   └── __init__.py
│
└── payments/                     # Main Django application
    ├── models.py                # Database models
    ├── views.py                 # View logic and calculations
    ├── forms.py                 # Django forms
    ├── urls.py                  # App URL patterns
    ├── admin.py                 # Django admin configuration
    ├── migrations/              # Database migrations
    ├── templates/
    │   └── payments/
    │       └── index.html       # Main template
    └── __init__.py
```

## Data Model

**PaymentRecord** includes:
- **date** (DateField): Appointment date
- **patient_name** (CharField): Patient's name
- **payment_method** (CharField): Payment type
- **amount** (DecimalField): Consultation fee
- **used_sigma** (BooleanField): Sigma insurance indicator

## Payment Methods Supported

| Method | Code | Commission |
|--------|------|-----------|
| Cash | `cash` | 0% |
| Clave | `clave` | 2% |
| Visa/MasterCard | `visa_mc` | 3% |
| Yappy | `yappy` | 1% |
| Sigma Insurance | `sigma` | 0% |

## Calculation Breakdown

### Example: $100 Payment via Visa

```
Gross Amount:           $100.00
Bank Commission (3%):   -$3.00
ITBMS (7% of comm):     -$0.21
Total Cobrado:          $96.79
Doctor Commission (40%): $38.72
```

## Deployment to PythonAnywhere

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

### Quick Summary:
1. Push to GitHub
2. Clone in PythonAnywhere
3. Install: `pip install -r requirements.txt`
4. Configure WSGI with SECRET_KEY and ALLOWED_HOSTS
5. Run migrations and collect static files
6. Reload web app

## Usage Instructions

### Recording a Payment

1. Fill in the form:
   - **Fecha de Cita** (Appointment Date)
   - **Nombre del Paciente** (Patient Name)
   - **Método de Pago** (Payment Method)
   - **Monto Cobrado** (Amount Charged)
   - **Sigma Insurance** (checkbox if applicable)

2. Click **Guardar Pago** (Save Payment)

### Viewing Reports

1. **Select Month**: Choose from available months in dropdown
2. **Payment Records**: All payments for selected month
3. **Totals by Method**: Revenue breakdown per payment method
4. **Commissions & Fees**: Bank commission, ITBMS, and net received
5. **Doctor Commission**: 40% calculation with regular/Sigma split

## Security Features

- ✓ CSRF protection enabled
- ✓ SQL injection protection (Django ORM)
- ✓ XSS protection (template escaping)
- ✓ Environment variable support for sensitive data
- ✓ Secure password validators
- ✓ SSL/HTTPS ready (settings.py configured for production)

## Environment Setup (Production)

Configure these environment variables in your PythonAnywhere WSGI file:

```python
os.environ['DEBUG'] = 'False'
os.environ['DJANGO_SECRET_KEY'] = 'your-secure-random-key'
os.environ['ALLOWED_HOSTS'] = 'your-domain.pythonanywhere.com'
```

## Maintenance

### Database Backups
```bash
cp db.sqlite3 backups/db_$(date +%Y%m%d).sqlite3
```

### Update Application
```bash
git pull origin main
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```

## Troubleshooting

### Migrations failed
```bash
python manage.py showmigrations
python manage.py migrate
```

### Static files not loading
```bash
python manage.py collectstatic --clear --noinput
```

### Reset database (dev only)
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## Documentation

- **Django**: https://docs.djangoproject.com/
- **PythonAnywhere**: https://www.pythonanywhere.com/help/
- **SQLite**: https://www.sqlite.org/docs.html

## License

Created for Dra. Michelle Echeverry's medical practice.

---

**Last Updated**: March 2026
**Python Version**: 3.10+
**Django Version**: 6.0.3