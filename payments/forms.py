from django import forms
from .models import PaymentRecord


class PaymentRecordForm(forms.ModelForm):
    class Meta:
        model = PaymentRecord
        fields = ['date', 'patient_name', 'payment_method', 'amount', 'used_sigma']
        labels = {
            'date': 'Fecha de Cita',
            'patient_name': 'Nombre del Paciente',
            'payment_method': 'Método de Pago',
            'amount': 'Monto Cobrado ($)',
            'used_sigma': 'Paciente utilizó seguro Sigma',
        }
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input'
            }),
            'patient_name': forms.TextInput(attrs={
                'type': 'text',
                'placeholder': 'Nombre del Paciente',
                'class': 'form-input'
            }),
            'payment_method': forms.Select(attrs={
                'class': 'form-select'
            }),
            'amount': forms.NumberInput(attrs={
                'type': 'number',
                'placeholder': '0.00',
                'step': '0.01',
                'class': 'form-input'
            }),
            'used_sigma': forms.CheckboxInput(attrs={
                'class': 'form-checkbox'
            }),
        }
