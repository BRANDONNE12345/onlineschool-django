from django import forms
from .models import Course, Chapter, Content, Quiz, Question, Option

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class ChapterForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['content_type', 'text_content', 'file_content']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ajout d'une classe CSS à chaque champ pour faciliter l'intégration avec Bootstrap
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'number_of_attempts', 'auto_correction']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text', 'is_correct']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Pour le champ is_correct, vous pouvez conserver le widget par défaut (checkbox)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
