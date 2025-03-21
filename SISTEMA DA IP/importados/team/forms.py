# team/forms.py
from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = [
            'nome', 
            'cargo',
            'departamento',
            'telefone',
            'email',
            'data_admissao',
            'observacoes',
        ]
        widgets = {
            'data_admissao': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
