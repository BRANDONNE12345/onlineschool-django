from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Course, Forum
from .forms import CourseForm

@login_required
def create_course(request):
    # Vérifier que seul un enseignant peut créer un cours
    if request.user.role != 'ENSEIGNANT':
        return HttpResponseForbidden("Vous n'êtes pas autorisé à créer un cours.")
    
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.is_validated = False  # Le cours doit être validé par le responsable
            course.save()
            # Création automatique d'un forum associé au cours
            Forum.objects.create(course=course, title=f"Forum de {course.title}")
            return redirect('courses:course_detail', course_id=course.id)
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Récupération des chapitres, quiz et forum pour l'affichage
    chapters = course.chapters.all()
    quizzes = course.quizzes.all()
    forum = getattr(course, 'forum', None)
    context = {
        'course': course,
        'chapters': chapters,
        'quizzes': quizzes,
        'forum': forum,
    }
    return render(request, 'courses/course_detail.html', context)
