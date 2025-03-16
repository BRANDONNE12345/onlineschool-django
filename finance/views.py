from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payment, Salary
from .forms import PaymentForm, SalaryForm

# Vue pour créer un paiement
@login_required
def create_payment(request):
    # On peut limiter cette action aux membres du service de comptabilité si besoin
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:payment_list')
    else:
        form = PaymentForm()
    return render(request, 'finance/create_payment.html', {'form': form})

# Vue pour afficher la liste des paiements
@login_required
def payment_list(request):
    payments = Payment.objects.all().order_by('-date')
    return render(request, 'finance/payment_list.html', {'payments': payments})

# Vue pour créer une fiche de salaire
@login_required
def create_salary(request):
    # On peut limiter cette action aux utilisateurs du service de comptabilité
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:salary_list')
    else:
        form = SalaryForm()
    return render(request, 'finance/create_salary.html', {'form': form})

# Vue pour afficher la liste des salaires
@login_required
def salary_list(request):
    salaries = Salary.objects.all().order_by('-date')
    return render(request, 'finance/salary_list.html', {'salaries': salaries})
