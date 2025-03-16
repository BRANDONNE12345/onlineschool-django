from django.db import models
from django.conf import settings

class ChatDeClasse(models.Model):
    classe = models.CharField(max_length=255)

    def __str__(self):
        return f"Chat de {self.classe}"

class MessageClasse(models.Model):
    chat = models.ForeignKey(ChatDeClasse, on_delete=models.CASCADE, related_name="messages")
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auteur.username}: {self.contenu[:50]}..."

class ChatB2B(models.Model):
    etudiant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="chats_etu")
    enseignant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="chats_prof")

    def __str__(self):
        return f"Chat {self.etudiant.username} - {self.enseignant.username}"

class MessageB2B(models.Model):
    chat = models.ForeignKey(ChatB2B, on_delete=models.CASCADE, related_name="messages")
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_envoye = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.auteur.username}: {self.contenu[:50]}..."
