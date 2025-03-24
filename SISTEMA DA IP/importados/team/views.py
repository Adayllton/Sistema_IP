# team/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TeamMember
from .forms import TeamMemberForm

@login_required(login_url='/users/login/')
def membros_view(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team:membros')
    else:
        form = TeamMemberForm()
    membros = TeamMember.objects.all().order_by('nome')
    return render(request, 'team/membros.html', {'form': form, 'membros': membros})

@login_required(login_url='/users/login/')
def editar_membro(request, membro_id):
    membro = get_object_or_404(TeamMember, pk=membro_id)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, instance=membro)
        if form.is_valid():
            form.save()
            return redirect('team:membros')
    else:
        form = TeamMemberForm(instance=membro)
    return render(request, 'team/editar_membro.html', {'form': form, 'membro': membro})