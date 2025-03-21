from django.db import models
from django.conf import settings

class Report(models.Model):
    TIPO_CHOICES = [
        ('semanal', 'Semanal'),
        ('mensal', 'Mensal'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data = models.DateField()

    # Campos comuns
    feedback_geral = models.TextField(help_text="Feedback geral do período")
    acao_correcao_semana = models.TextField(
        blank=True, null=True,
        help_text="O que podemos fazer para corrigir os erros da semana?"
    )
    
    # Novos campos para atendimento
    atendimento_presencial = models.TextField(
        blank=True, null=True,
        help_text="Feedback e avaliação do atendimento presencial"
    )
    atendimento_online = models.TextField(
        blank=True, null=True,
        help_text="Feedback e avaliação do atendimento online"
    )

    # Exclusivos do relatório semanal
    produtos_mais_procurados = models.TextField(
        blank=True, null=True,
        help_text="Produtos mais procurados (exclusivo do semanal)"
    )

    # Exclusivos do relatório mensal (mais detalhados)
    sugestao_grade_produtos = models.TextField(
        blank=True, null=True,
        help_text="Sugestão de retirada ou inserção na grade de produtos da loja"
    )
    acao_melhoria_mes = models.TextField(
        blank=True, null=True,
        help_text="O que fazer para melhorar esse mês"
    )
    colaborador_destaque = models.CharField(
        max_length=100, blank=True, null=True,
        help_text="Colaborador do mês com destaque dos principais fatores"
    )
    feedback_organizacao = models.TextField(
        blank=True, null=True,
        help_text="Feedback sobre a organização da loja (produtos expostos, vitrine, limpeza, etc.)"
    )
    logistica = models.TextField(
        blank=True, null=True,
        help_text="O que pode melhorar na logística"
    )

    # Relação com o usuário que criou o relatório
    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.data}"
