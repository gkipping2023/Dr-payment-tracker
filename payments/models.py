from django.db import models


class PaymentRecord(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('clave', 'Clave'),
        ('visa_mc', 'Visa/MasterCard'),
        ('yappy', 'Yappy'),
        ('sigma', 'Sigma'),
    ]

    date = models.DateField()
    patient_name = models.CharField(max_length=200)
    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD_CHOICES
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    used_sigma = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.patient_name} - {self.date}"
