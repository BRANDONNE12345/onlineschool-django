from django.shortcuts import render
from .models import Payment, Salary

def finance_dashboard(request):
    payments = Payment.objects.all()
    salaries = Salary.objects.all()

    context = {
        'payments': payments,
        'salaries': salaries,
        'total_paiements': sum(p.amount for p in payments),
        'total_salaires': sum(s.amount for s in salaries),
        'dernier_paiement': payments.order_by('-date').first(),
        'dernier_salaire': salaries.order_by('-date').first(),
    }
    return render(request, 'finance/finance_dashboard.html', context)
