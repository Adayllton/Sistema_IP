"""
URL configuration for importados project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Rota para a página inicial
    path('tarefas/', include('tarefas.urls')),
    path('users/', include('users.urls')),
    path('reports/', include('reports.urls')),
    path('team/', include('team.urls')),
    # Redireciona a raiz para a página de login
    path('', RedirectView.as_view(url='/users/login/', permanent=False)),
    path('calculator/', include('calculator.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



