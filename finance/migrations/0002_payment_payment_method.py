# Generated by Django 5.1.7 on 2025-03-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('CASH', 'Espèces'), ('WAVE', 'Wave'), ('OM', 'Orange Money'), ('CARD', 'Carte bancaire')], default='CASH', max_length=10),
        ),
    ]
