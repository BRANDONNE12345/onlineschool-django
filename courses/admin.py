from django.contrib import admin
from .models import (
    Course, Chapter, Content, Quiz, Question, Option, Forum, Message
)

# Inline pour gérer les contenus au sein d'un chapitre
class ContentInline(admin.TabularInline):
    model = Content
    extra = 1

# Admin pour Chapter avec l'inclusion des contenus (Content)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__title')
    inlines = [ContentInline]

# Inline pour gérer les chapitres directement depuis un cours
class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'is_validated', 'created_at')
    list_filter = ('is_validated', 'teacher')
    search_fields = ('title', 'description', 'teacher__username')
    ordering = ('title',)
    inlines = [ChapterInline]  # Permet d'ajouter/modifier les chapitres dans la fiche du cours

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'number_of_attempts', 'auto_correction')
    list_filter = ('auto_correction',)
    search_fields = ('title', 'course__title')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    search_fields = ('text',)

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('course', 'title', 'created_at')
    search_fields = ('title', 'course__title')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('forum', 'author', 'created_at')
    search_fields = ('author__username', 'content')

# Enregistrement séparé de Chapter pour pouvoir le gérer de manière indépendante
admin.site.register(Chapter, ChapterAdmin)
