# reports/forms.py
from django import forms
from .models import Report

from django import forms
from .models import Report

class ReportWeeklyForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'data',
            'feedback_geral',
            'acao_correcao_semana',
            'produtos_mais_procurados',  # já existente para o semanal
            'atendimento_presencial',
            'atendimento_online',
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'feedback_geral': forms.Textarea(attrs={'rows': 3}),
            'acao_correcao_semana': forms.Textarea(attrs={'rows': 3}),
            'produtos_mais_procurados': forms.Textarea(attrs={'rows': 3}),
            'atendimento_presencial': forms.Textarea(attrs={'rows': 3}),
            'atendimento_online': forms.Textarea(attrs={'rows': 3}),
        }


class ReportMonthlyForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'data',
            'feedback_geral',
            'acao_correcao_semana',
            'sugestao_grade_produtos',
            'acao_melhoria_mes',
            'colaborador_destaque',
            'feedback_organizacao',
            'logistica',
            'atendimento_presencial',
            'atendimento_online',
        ]
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'feedback_geral': forms.Textarea(attrs={'rows': 3}),
            'acao_correcao_semana': forms.Textarea(attrs={'rows': 3}),
            'sugestao_grade_produtos': forms.Textarea(attrs={'rows': 3}),
            'acao_melhoria_mes': forms.Textarea(attrs={'rows': 3}),
            'feedback_organizacao': forms.Textarea(attrs={'rows': 3}),
            'logistica': forms.Textarea(attrs={'rows': 3}),
            'atendimento_presencial': forms.Textarea(attrs={'rows': 3}),
            'atendimento_online': forms.Textarea(attrs={'rows': 3}),
        }
