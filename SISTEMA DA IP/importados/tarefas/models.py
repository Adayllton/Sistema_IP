# tarefas/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone

class Board(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='lists')
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.board.name} - {self.name}"

class Task(models.Model):
    lista = models.ForeignKey(List, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    assigned_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='tasks')
    order = models.PositiveIntegerField(default=0)  # para a ordenação com SortableJS

    def __str__(self):
        return self.title

    def deadline_status(self):
        today = timezone.now().date()
        if self.due_date > today:
            delta = self.due_date - today
            return f"Faltam {delta.days} dias"
        elif self.due_date < today:
            delta = today - self.due_date
            return f"Excedeu {delta.days} dias"
        else:
            return "Prazo final hoje"

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comentário por {self.user} em {self.task}"

class TaskHistory(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='history')
    action = models.CharField(max_length=100)
    performed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True)
    def __str__(self):
        return f"{self.action} em {self.task.title} por {self.performed_by}"
    
class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anexo para {self.task.title}"

