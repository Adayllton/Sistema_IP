from django.db import models

# Create your models here.
# team/models.py
from django.db import models
from reports.models import Report

# team/models.py
from django.db import models

class TeamMember(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    data_admissao = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo or ''}"


class Evaluation(models.Model):
    TIPO_AVALIACAO_CHOICES = [
        ('semanal', 'Semanal'),
        ('mensal', 'Mensal'),
    ]
    
    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, related_name="evaluations"
    )
    team_member = models.ForeignKey(
        TeamMember, on_delete=models.CASCADE, related_name="evaluations"
    )
    tipo_avaliacao = models.CharField(
        max_length=10, choices=TIPO_AVALIACAO_CHOICES
    )
    nota = models.IntegerField(
        help_text="Avaliação de 1 a 5"
    )
    comentario = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.team_member.nome} - {self.tipo_avaliacao} - {self.nota}"
