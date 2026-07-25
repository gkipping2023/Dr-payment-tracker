# Django settings local imports
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    os.getenv(
        "DJANGO_SETTINGS_MODULE",
        "doctor_payments.settings.development",
    ),
)