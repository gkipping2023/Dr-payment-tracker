from django.contrib import admin
from .models import PaymentRecord


@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'patient_name', 'payment_method', 'amount', 'used_sigma')
    list_filter = ('date', 'payment_method', 'used_sigma')
    search_fields = ('patient_name',)
    ordering = ('-date',)
