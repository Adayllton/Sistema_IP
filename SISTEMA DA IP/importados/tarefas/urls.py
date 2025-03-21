from django.urls import path
from .views import (
    BoardListView, BoardDetailView, BoardCreateView, BoardUpdateView, BoardDeleteView,
    TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, ListCreateView, add_attachment, mark_task_completed, update_task_order, add_comment
)
app_name = 'tarefas'

urlpatterns = [
    path('', BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>/', BoardDetailView.as_view(), name='board_detail'),
    path('board/criar/', BoardCreateView.as_view(), name='board_create'),
    path('board/editar/<int:pk>/', BoardUpdateView.as_view(), name='board_update'),
    path('board/excluir/<int:pk>/', BoardDeleteView.as_view(), name='board_delete'),

    # Tarefas
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/criar/', TaskCreateView.as_view(), name='task_create'),
    path('task/editar/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task/excluir/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:task_id>/comment/', add_comment, name='add_comment'),
    path('task/update_order/', update_task_order, name='update_task_order'),
    path('task/mark_completed/<int:pk>/', mark_task_completed, name='mark_task_completed'),
    path('task/<int:task_id>/attachment/add/', add_attachment, name='add_attachment'),


    # Lists
    path('list/criar/', ListCreateView.as_view(), name='list_create'),
]
