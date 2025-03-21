from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm  # Importa o formulário customizado

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('reports:report_list')
            else:
                messages.error(request, "Usuário ou senha inválidos.")
        else:
            messages.error(request, "Dados inválidos. Tente novamente.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def cadastro_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use o formulário customizado
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso. Faça login para continuar.")
            return redirect('users:login')
        else:
            messages.error(request, "Erro no cadastro. Verifique os dados e tente novamente.")
    else:
        form = CustomUserCreationForm()  # Use o formulário customizado
    return render(request, 'users/cadastro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('users:login')
