from django.db import models
from users.models import User

PAYMENT_METHOD_CHOICES = [
    ('CASH', 'Espèces'),
    ('WAVE', 'Wave'),
    ('OM', 'Orange Money'),
    ('CARD', 'Carte bancaire'),
]

class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='CASH')

    def __str__(self):
        return f"Paiement de {self.amount}€ pour {self.student.username} le {self.date.strftime('%Y-%m-%d')}"


class Salary(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="salaries")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Salaire de {self.amount}€ pour {self.teacher.username} le {self.date.strftime('%Y-%m-%d')}"
