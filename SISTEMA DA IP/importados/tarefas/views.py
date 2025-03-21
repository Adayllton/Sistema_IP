from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Board, Task, TaskHistory
from .forms import BoardForm, ListForm, TaskForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from .models import Task, Board, List
from .forms import TaskForm
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Task
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Attachment
from .forms import AttachmentForm

def add_attachment(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.task = task
            attachment.save()
            return redirect('tarefas:task_detail', pk=task.pk)
    else:
        form = AttachmentForm()
    return render(request, 'tarefas/attachment_form.html', {'form': form, 'task': task})


@login_required
def mark_task_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    # Aqui você pode adicionar regras de permissão, se necessário
    task.status = 'concluida'
    task.save()
    # Opcional: registre no histórico
    from .models import TaskHistory
    TaskHistory.objects.create(
        task=task,
        action="Concluída",
        performed_by=request.user,
        details="Tarefa marcada como concluída."
    )
    return redirect('tarefas:task_detail', pk=pk)

@require_POST
def update_task_order(request):
    data = json.loads(request.body)
    list_id = data.get('list_id')
    order = data.get('order', [])
    for index, task_id in enumerate(order):
        try:
            task = Task.objects.get(pk=task_id)
            # Se a tarefa foi movida para outra lista, atualize também
            if str(task.lista.pk) != str(list_id):
                task.lista_id = list_id
            task.order = index
            task.save()
        except Task.DoesNotExist:
            continue
    return JsonResponse({'status': 'success'})

class BoardListView(ListView):
    model = Board
    template_name = 'tarefas/board_list.html'
    context_object_name = 'boards'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(name__icontains=q)
        return queryset

class BoardDetailView(DetailView):
    model = Board
    template_name = 'tarefas/board_detail.html'
    context_object_name = 'board'

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comment_form = CommentForm()
    return render(request, 'tarefas/task_detail.html', {'task': task, 'comment_form': comment_form})

def add_comment(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            # Salvar ação no histórico
            TaskHistory.objects.create(task=task, action='Comentou', performed_by=request.user, details=comment.text)
    return redirect('tarefas:task_detail', pk=task.id)

# tarefas/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Board, Task
from .forms import BoardForm, TaskForm

# CRUD para Board
class BoardListView(ListView):
    model = Board
    template_name = 'tarefas/board_list.html'
    context_object_name = 'boards'

class BoardDetailView(DetailView):
    model = Board
    template_name = 'tarefas/board_detail.html'
    context_object_name = 'board'

class BoardCreateView(CreateView):
    model = Board
    form_class = BoardForm
    template_name = 'tarefas/board_form.html'
    success_url = reverse_lazy('tarefas:board_list')

class BoardUpdateView(UpdateView):
    model = Board
    form_class = BoardForm
    template_name = 'tarefas/board_form.html'
    success_url = reverse_lazy('tarefas:board_list')

class BoardDeleteView(DeleteView):
    model = Board
    template_name = 'tarefas/board_confirm_delete.html'
    success_url = reverse_lazy('tarefas:board_list')

# CRUD para Task
class TaskDetailView(DetailView):
    model = Task
    template_name = 'tarefas/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tarefas/task_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Captura o board_id da query string, se existir
        board_id = self.request.GET.get('board')
        context['board_id'] = board_id
        return context

    def get_success_url(self):
        # Após salvar, redireciona para o detalhe do quadro (assumindo que a tarefa está associada à lista e essa lista pertence a um board)
        return reverse_lazy('tarefas:board_detail', kwargs={'pk': self.object.lista.board.pk})

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tarefas/task_form.html'

    def test_func(self):
        # Permite que apenas o criador ou admin edite (exemplo)
        return self.request.user.is_staff or self.request.user in self.get_object().assigned_users.all()

    def get_success_url(self):
        return reverse_lazy('tarefas:board_detail', kwargs={'pk': self.object.list.board.pk})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tarefas/task_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('tarefas:board_detail', kwargs={'pk': self.object.lista.board.pk})

    

class ListCreateView(CreateView):
    model = List
    form_class = ListForm
    template_name = 'tarefas/list_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtém o board_id da query string para exibir no template
        context['board_id'] = self.request.GET.get('board')
        return context

    def form_valid(self, form):
        # Associa a nova lista ao quadro cujo id foi passado na URL
        board_id = self.request.GET.get('board')
        board = get_object_or_404(Board, pk=board_id)
        form.instance.board = board
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('tarefas:board_detail', kwargs={'pk': self.object.board.pk})

