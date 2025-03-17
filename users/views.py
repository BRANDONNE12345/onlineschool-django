from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()  # Récupère le modèle utilisateur personnalisé

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Inscription réussie ! Connectez-vous maintenant.")
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "user/register.html", {"form": form})

class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        if not user.is_approved:
            messages.error(self.request, "Votre compte n'est pas encore validé par l'administrateur.")
            return redirect("login")
        return super().form_valid(form)

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'users/edit_profile.html', {'form': form})
