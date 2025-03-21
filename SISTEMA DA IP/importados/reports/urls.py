# reports/urls.py
from django.urls import path
from .views import (
    ReportWeeklyCreateView, 
    ReportMonthlyCreateView, 
    ReportListView,
    ReportUpdateView,
    ReportDeleteView,
    ReportDetailView,
    export_report_pdf,
)

app_name = 'reports'

urlpatterns = [
    path('novo/semanal/', ReportWeeklyCreateView.as_view(), name='report_create_weekly'),
    path('novo/mensal/', ReportMonthlyCreateView.as_view(), name='report_create_monthly'),
    path('lista/', ReportListView.as_view(), name='report_list'),
    path('editar/<int:pk>/', ReportUpdateView.as_view(), name='report_update'),
    path('excluir/<int:pk>/', ReportDeleteView.as_view(), name='report_delete'),
    path('visualizar/<int:pk>/', ReportDetailView.as_view(), name='report_view'),
    path('exportar/<int:pk>/', export_report_pdf, name='report_export_pdf'),

]
