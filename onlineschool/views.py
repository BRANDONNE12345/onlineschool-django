from django.http import HttpResponse
from django.shortcuts import render
from finance.models import Payment, Salary 
from courses.models import Course
from users.models import User



def index(request):
    return render(request, 'index.html')  # Assure-toi que 'index.html' est bien placé

def dashboard_etudiant(request):
    return render(request, 'dashboard_etudiant.html')  

def dashboard_finance(request):
    payments = Payment.objects.all()  # Récupère tous les paiements
    salaries = Salary.objects.all()  # Récupère tous les salaires
    return render(request, 'dashboard_finance.html', {'payments': payments, 'salaries': salaries})


def dashboard_enseignant(request):
    # Récupère le premier utilisateur avec le rôle "ENSEIGNANT"
    user = User.objects.filter(role='ENSEIGNANT').first()
    
    if user is None:
        # Si aucun enseignant n'est trouvé, tu peux renvoyer une erreur ou un message
        return HttpResponse("Aucun enseignant trouvé", status=404)
    
    # Récupère les cours de cet enseignant
    courses = Course.objects.filter(teacher=user)
    return render(request, 'dashboard_enseignant.html', {'courses': courses})



def course(request):
    return render(request,'course.html')


def about(request): 
    return render(request,'about.html')

def contact(request): 
    return render(request,'contact.html')

def team(request): 
    return render(request,'team.html')
    

