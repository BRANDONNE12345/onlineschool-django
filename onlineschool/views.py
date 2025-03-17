from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Assure-toi que 'index.html' est bien placé

def dashboard_etudiant(request):
    return render(request, 'dashboard_etudiant.html')  

def dashboard_finance(request):
    return render(request, 'dashboard_finance.html')


def dashboard_enseignant(request):
    # Vous pouvez également ajouter ici les variables de contexte nécessaires (par exemple, courses, quizzes, forum_messages, etc.)
    return render(request, 'dashboard_enseignant.html')


def course(request):
    return render(request,'course.html')
