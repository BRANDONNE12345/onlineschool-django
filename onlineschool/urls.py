"""
URL configuration for onlineschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from onlineschool import views
from .views import login_view, logout_view
from users.views import register

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('dashboard/etudiant/', views.dashboard_etudiant, name='dashboard_etudiant'),
    path('dashboard/finance/', views.dashboard_finance, name='dashboard_finance'),
    path('dashboard/enseignant/', views.dashboard_enseignant, name='dashboard_enseignant'),
    
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('finance/', include('finance.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('register/', register, name='register'),


]
