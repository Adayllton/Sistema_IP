from django.urls import path
from .views import index

app_name = 'calculator'

urlpatterns = [
    path('', index, name='index'),
]
