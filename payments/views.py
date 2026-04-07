from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.db.models import Sum
from decimal import Decimal
from datetime import date
from .models import PaymentRecord
from .forms import PaymentRecordForm


@require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        form = PaymentRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments:index')
    else:
        form = PaymentRecordForm()

    today = date.today()

    # Get all unique year-month combinations from payments
    all_payments = PaymentRecord.objects.all().order_by('-date')
    available_months = []
    seen_months = set()

    for payment in all_payments:
        month_key = payment.date.strftime('%Y-%m')
        if month_key not in seen_months:
            available_months.append({
                'value': month_key,
                'display': payment.date.strftime('%B %Y')
            })
            seen_months.add(month_key)

    # Default to current month if no payments exist
    if not available_months:
        current_month = today.strftime('%Y-%m')
        available_months.append({
            'value': current_month,
            'display': today.strftime('%B %Y')
        })

    month_param = request.GET.get('month', available_months[0]['value'])

    try:
        year = int(month_param[:4])
        month = int(month_param[5:7])
        if not (1 <= month <= 12):
            raise ValueError
    except (ValueError, IndexError):
        year, month = today.year, today.month

    selected_month = f"{year:04d}-{month:02d}"
    selected_month_display = date(year, month, 1).strftime('%B %Y')

    payments = PaymentRecord.objects.filter(
        date__year=year, date__month=month
    ).order_by('-date')

    total_amount = payments.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')

    totals_by_method = list(payments.values('payment_method').annotate(
        total=Sum('amount')
    ).order_by('payment_method'))

    # Calculate commissions and ITBMS for each payment method
    commission_rates = {
        'clave': Decimal('0.02'),
        'visa_mc': Decimal('0.03'),
        'yappy': Decimal('0.01'),
        'sigma': Decimal('0.00'),
    }

    for row in totals_by_method:
        method = row['payment_method']
        total = row['total']

        # Get commission rate, default to 0% (cash, etc.)
        commission_rate = commission_rates.get(method, Decimal('0.00'))

        # Calculate commission and ITBMS
        commission = total * commission_rate
        itbms = commission * Decimal('0.07')
        total_cobrado = total - commission - itbms

        row['commission'] = commission
        row['itbms'] = itbms
        row['total_cobrado'] = total_cobrado

    # Calculate totals for commissions table
    total_commission = sum(row['commission'] for row in totals_by_method)
    total_itbms = sum(row['itbms'] for row in totals_by_method)
    total_cobrado_all = sum(row['total_cobrado'] for row in totals_by_method)

    # Calculate doctor commission (40% of total_cobrado_all)
    doctor_commission = total_cobrado_all * Decimal('0.40')


    # Get SIGMA payment method total
    sigma_total = Decimal('0.00')
    for row in totals_by_method:
        if row['payment_method'] == 'sigma':
            sigma_total = row['total']
            break

    # Calculate 40% of SIGMA total
    sigma_commission = sigma_total * Decimal('0.40')

    # Calculate Regular comision (total doctor commission - sigma commission)
    regular_commission = doctor_commission - sigma_commission

    context = {
        'form': form,
        'payments': payments,
        'total_amount': total_amount,
        'totals_by_method': totals_by_method,
        'total_commission': total_commission,
        'total_itbms': total_itbms,
        'total_cobrado_all': total_cobrado_all,
        'doctor_commission': doctor_commission,
        'sigma_commission': sigma_commission,
        'regular_commission': regular_commission,
        'selected_month': selected_month,
        'selected_month_display': selected_month_display,
        'available_months': available_months,
    }

    return render(request, 'payments/index.html', context)


@require_http_methods(["POST"])
def delete_payment(request, payment_id):
    payment = get_object_or_404(PaymentRecord, pk=payment_id)
    payment.delete()
    return redirect('payments:index')
