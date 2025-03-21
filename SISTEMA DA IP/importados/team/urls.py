# team/urls.py
from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('membros/', views.membros_view, name='membros'),
    path('membros/editar/<int:membro_id>/', views.editar_membro, name='editar_membro'),
]
