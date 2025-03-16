from django.db import models
from users.models import User

# ---------------------
# Modèle Course
# ---------------------
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses", limit_choices_to={'role': 'ENSEIGNANT'})
    is_validated = models.BooleanField(default=False)
    validated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="validated_courses", limit_choices_to={'role': 'SCOLARITE'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

# ---------------------
# Modèle Chapter
# ---------------------
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.title} ({self.course.title})"

# ---------------------
# Modèle Content
# ---------------------
CONTENT_TYPE_CHOICES = [
    ('TEXT', 'Texte enrichi'),
    ('IMAGE', 'Image/Infographie'),
    ('PDF', 'Document PDF'),
    ('VIDEO', 'Vidéo'),
]

class Content(models.Model):
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name="contents")
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)
    text_content = models.TextField(blank=True, null=True)
    file_content = models.FileField(upload_to='contents/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_content_type_display()} dans {self.chapter.title}"



# permet de savoir quels étudiants suivent quels cours.

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrollments", limit_choices_to={'role': 'ETUDIANT'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} inscrit à {self.course.title}"

# ---------------------
# Modèles pour Quiz et Évaluation
# ---------------------
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=200)
    number_of_attempts = models.IntegerField(default=1)
    auto_correction = models.BooleanField(default=True)
    duration = models.PositiveIntegerField(default=30)  # Durée en minutes

    def __str__(self):
        return self.title


QUESTION_TYPE_CHOICES = [
    ('TEXT', 'Réponse texte libre'),
    ('MCQ', 'Choix multiple'),
]

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPE_CHOICES, default='MCQ')

    def __str__(self):
        return f"Question pour {self.quiz.title}"

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=300)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Option pour '{self.question.text[:30]}...'"
        
# ---------------------
# Modèles pour Forum et Messages
# ---------------------
class Forum(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name="forum")
    title = models.CharField(max_length=200, default="Forum du cours")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Forum de {self.course.title}"

class Message(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="messages")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message de {self.author.username} le {self.created_at.strftime('%Y-%m-%d %H:%M')}"
