from django import forms
from .models import Payment, Salary

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'amount', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajout d'une classe CSS pour une meilleure intégration (optionnel)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['teacher', 'amount', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
