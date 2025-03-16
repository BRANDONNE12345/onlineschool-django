from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [

    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('create/', views.create_course, name='create_course'),
    path('chapter/create/', views.create_chapter, name='create_chapter'),
    path('forum/create/', views.create_forum, name='create_forum'),
    path('option/create/', views.create_option, name='create_option'),
    path('question/create/', views.create_question, name='create_question'),
    path('quiz/create/', views.create_quiz, name='create_quiz'),
]
