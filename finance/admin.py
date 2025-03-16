from django.contrib import admin
from .models import Payment, Salary

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'date')
    list_filter = ('date',)
    search_fields = ('student__username', 'description')
    ordering = ('-date',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'amount', 'date')
    list_filter = ('date',)
    search_fields = ('teacher__username', 'description')
    ordering = ('-date',)
