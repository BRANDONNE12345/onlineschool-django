from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Définition des choix de rôles
    ROLE_CHOICES = [
        ('ADMIN', 'Administrateur'),
        ('SCOLARITE', 'Responsable de scolarité'),
        ('ENSEIGNANT', 'Enseignant'),
        ('ETUDIANT', 'Étudiant'),
        ('teacher', 'Enseignant'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='ETUDIANT')
    is_approved = models.BooleanField(default=False)
    email = models.EmailField(unique=True)  # Assure-toi que l'email est unique
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    # Méthodes personnalisées (facultatives)
    def se_connecter(self):
        # La logique de connexion est gérée par Django, mais vous pouvez ajouter des loggings ou d'autres actions ici
        pass

    def se_deconnecter(self):
        # Pareil pour la déconnexion
        pass