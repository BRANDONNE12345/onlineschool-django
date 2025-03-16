from django.db import models
from users.models import User

class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name="chats")
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="messages")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    def __str__(self):
        return f"Message de {self.author.username} le {self.created_at.strftime('%Y-%m-%d %H:%M')}"

