from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
]
