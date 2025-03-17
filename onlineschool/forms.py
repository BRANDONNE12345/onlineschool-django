from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()  # Récupère le modèle d'utilisateur personnalisé

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Utilise le modèle d'utilisateur personnalisé
        fields = ('username', 'email', 'password1', 'password2')  # Champs à inclure dans le formulaire