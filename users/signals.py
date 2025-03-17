from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User

@receiver(post_save, sender=User)
def send_approval_email(sender, instance, **kwargs):
    if instance.is_approved and instance.is_active:
        send_mail(
            "Votre compte est maintenant activé",
            "Bonjour {},\n\nVotre compte a été approuvé par un administrateur. Vous pouvez maintenant vous connecter.\n\nMerci !".format(instance.username),
            "admin@onlineschool.com",
            [instance.email],
            fail_silently=False,
        )
