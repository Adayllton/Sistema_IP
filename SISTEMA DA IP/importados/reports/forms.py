from django import forms
from .models import Report

class ReportWeeklyForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'data',
            'feedback_geral',
            'acao_correcao_semana',
            'produtos_mais_procurados',
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
        labels = {
            'data': 'Data',
            'feedback_geral': 'Feedback Geral',
            'acao_correcao_semana': 'Ação de Correção Semanal',
            'produtos_mais_procurados': 'Produtos Mais Procurados',
            'atendimento_presencial': 'Atendimento Presencial',
            'atendimento_online': 'Atendimento Online',
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
        labels = {
            'data': 'Data',
            'feedback_geral': 'Feedback Geral',
            'acao_correcao_semana': 'Ação de Correção Semanal',
            'sugestao_grade_produtos': 'Sugestão de Grade de Produtos',
            'acao_melhoria_mes': 'Ação de Melhoria do Mês',
            'colaborador_destaque': 'Colaborador Destaque',
            'feedback_organizacao': 'Feedback da Organização',
            'logistica': 'Logística',
            'atendimento_presencial': 'Atendimento Presencial',
            'atendimento_online': 'Atendimento Online',
        }
