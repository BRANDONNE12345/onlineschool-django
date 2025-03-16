from optparse import Option
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Course, Forum, Chapter, Question, Quiz
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

@login_required
def create_chapter(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        chapter_title = request.POST.get('chapter_title')
        course = get_object_or_404(Course, id=course_id)
        # Créez le chapitre
        Chapter.objects.create(course=course, title=chapter_title)
        return redirect('courses:course_detail', course_id=course.id)
    else:
        # On peut filtrer par enseignant ici, par exemple
        courses = Course.objects.all()
        return render(request, 'courses/create_chapter.html', {'courses': courses})

@login_required
def create_forum(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        forum_title = request.POST.get('forum_title')
        course = get_object_or_404(Course, id=course_id)
        # Créez le forum
        Forum.objects.create(course=course, title=forum_title)
        return redirect('courses:course_detail', course_id=course.id)
    else:
        # Par exemple, afficher la liste des cours pour selection
        courses = Course.objects.all()
        return render(request, 'courses/create_forum.html', {'courses': courses})
@login_required
def create_option(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        option_text = request.POST.get('option_text')
        is_correct = 'is_correct' in request.POST
        question = get_object_or_404(Question, id=question_id)
        Option.objects.create(question=question, text=option_text, is_correct=is_correct)
        # Redirigez vers une page appropriée, par exemple le détail du quiz ou de la question
        return redirect('courses:quiz_detail', quiz_id=question.quiz.id)
    else:
        questions = Question.objects.all()  # ou filtrez selon l'enseignant
        return render(request, 'courses/create_option.html', {'questions': questions})
    
@login_required
def create_question(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        question_text = request.POST.get('question_text')
        question_type = request.POST.get('question_type')
        quiz = get_object_or_404(Quiz, id=quiz_id)
        Question.objects.create(quiz=quiz, text=question_text, question_type=question_type)
        return redirect('courses:quiz_detail', quiz_id=quiz.id)
    else:
        quizzes = Quiz.objects.all()
        return render(request, 'courses/create_question.html', {'quizzes': quizzes})
    
@login_required
def create_question(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        question_text = request.POST.get('question_text')
        question_type = request.POST.get('question_type')
        quiz = get_object_or_404(Quiz, id=quiz_id)
        # Créez la question
        Question.objects.create(quiz=quiz, text=question_text, question_type=question_type)
        return redirect('courses:quiz_detail', quiz_id=quiz.id)
    else:
        # Affiche la liste des quiz pour la sélection
        quizzes = Quiz.objects.all()
        return render(request, 'courses/create_question.html', {'quizzes': quizzes})
@login_required
def create_quiz(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        quiz_title = request.POST.get('quiz_title')
        number_of_attempts = request.POST.get('number_of_attempts')
        auto_correction = request.POST.get('auto_correction') == 'true'
        duration = request.POST.get('duration')
        course = get_object_or_404(Course, id=course_id)
        quiz = Quiz.objects.create(
            course=course,
            title=quiz_title,
            number_of_attempts=number_of_attempts,
            auto_correction=auto_correction,
            duration=duration
        )
        return redirect('courses:quiz_detail', quiz_id=quiz.id)
    else:
        courses = Course.objects.all()
        return render(request, 'courses/create_quiz.html', {'courses': courses})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    context = {
        'quiz': quiz,
        'questions': questions,
    }
    return render(request, 'courses/quiz_detail.html', context)
