from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('payments/', views.payment_list, name='payment_list'),
    path('payments/create/', views.create_payment, name='create_payment'),
    path('salaries/', views.salary_list, name='salary_list'),
    path('salaries/create/', views.create_salary, name='create_salary'),
]
