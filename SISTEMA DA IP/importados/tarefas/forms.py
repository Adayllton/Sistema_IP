# tarefas/forms.py
from django import forms
from .models import Board, List, Task, Comment, Attachment

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # Utilizando 'list' conforme definido no modelo
        fields = ['lista', 'title', 'description', 'due_date', 'status', 'assigned_users']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name', 'order']  # ou outros campos que seu modelo List possua

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file']

