# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from team.models import TeamMember

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email',)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        # Verifica se já existe um usuário com esse username
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")

        # Verifica se existe um membro na equipe com esse nome
        if not TeamMember.objects.filter(nome=username).exists():
            raise forms.ValidationError("Não existe um membro cadastrado com este nome.")
        
        return username
