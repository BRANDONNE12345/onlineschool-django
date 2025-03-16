from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Payment, Salary
from .forms import PaymentForm, SalaryForm

@login_required
def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:payment_list')
    else:
        form = PaymentForm()
    # Utilise le template dans onlineschool/templates/create_payment.html
    return render(request, 'create_payement.html', {'form': form})

@login_required
def payment_list(request):
    payments = Payment.objects.all().order_by('-date')
    # Supposez que votre template se trouve dans onlineschool/templates/payment_list.html
    return render(request, 'payment_list.html', {'payments': payments})

@login_required
def create_salary(request):
    if request.method == 'POST':
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finance:salary_list')
    else:
        form = SalaryForm()
    # Utilise le template dans onlineschool/templates/create_salary.html
    return render(request, 'create_salary.html', {'form': form})

@login_required
def salary_list(request):
    salaries = Salary.objects.all().order_by('-date')
    # Supposez que votre template se trouve dans onlineschool/templates/salary_list.html
    return render(request, 'salary_list.html', {'salaries': salaries})
