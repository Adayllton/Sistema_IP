# tarefas/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, TaskHistory

@receiver(post_save, sender=Task)
def log_task_change(sender, instance, created, **kwargs):
    action = "Criada" if created else "Atualizada"
    TaskHistory.objects.create(
        task=instance,
        action=f"Tarefa {action}",
        performed_by=instance.assigned_users.first() if instance.assigned_users.exists() else None,
        details=f"A tarefa '{instance.title}' foi {action.lower()}."
    )
