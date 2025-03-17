from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['user_role'] = user.role  # Stocke le rôle dans la session
            return redirect('index')  # Redirection vers la page d'accueil
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect")

    return render(request, "user/login.html")

def logout_view(request):
    logout(request)
    request.session.flush()  # Supprime la session
    return redirect('index') 

def index(request):
    return render(request, 'index.html')  # Assure-toi que 'index.html' est bien placé


@login_required
def dashboard_etudiant(request):
    if request.user.role != "ETUDIANT":
        return redirect('index')  # Redirection si mauvais rôle
    return render(request, 'dashboard_etudiant.html')

@login_required
def dashboard_enseignant(request):
    if request.user.role != "ENSEIGNANT":
        return redirect('index')
    return render(request, 'dashboard_enseignant.html')

@login_required
def dashboard_finance(request):
    if request.user.role != "SCOLARITE":
        return redirect('index')
    return render(request, 'dashboard_finance.html')
