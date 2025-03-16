from django.db import models
from users.models import User

class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Paiement de {self.amount}€ pour {self.student.username} le {self.date.strftime('%Y-%m-%d')}"

class Salary(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="salaries")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Salaire de {self.amount}€ pour {self.teacher.username} le {self.date.strftime('%Y-%m-%d')}"
