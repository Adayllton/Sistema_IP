# reports/views.py
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Report
from .forms import ReportWeeklyForm, ReportMonthlyForm# reports/views.py
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import Report
import os
from django.conf import settings
from .models import Report

class ReportWeeklyCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportWeeklyForm
    template_name = 'reports/relatorio_form.html'
    success_url = reverse_lazy('reports:report_list')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.tipo = 'semanal'  # Define o tipo como semanal
        return super().form_valid(form)

class ReportMonthlyCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportMonthlyForm
    template_name = 'reports/relatorio_form.html'
    success_url = reverse_lazy('reports:report_list')

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.tipo = 'mensal'  # Define o tipo como mensal
        return super().form_valid(form)

class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/relatorio_list.html'
    context_object_name = 'reports'
    ordering = ['-data']

    def get_queryset(self):
        queryset = super().get_queryset()
        tipo = self.request.GET.get('tipo')
        if tipo in ['semanal', 'mensal']:
            queryset = queryset.filter(tipo=tipo)
        return queryset

class ReportUpdateView(LoginRequiredMixin, UpdateView):
    model = Report
    template_name = 'reports/relatorio_form.html'
    success_url = reverse_lazy('reports:report_list')
    context_object_name = 'report'

    def get_form_class(self):
        # Seleciona o formulário de acordo com o tipo do relatório
        report = self.get_object()
        if report.tipo == 'semanal':
            return ReportWeeklyForm
        else:
            return ReportMonthlyForm

    def form_valid(self, form):
        # Mantém o usuário que criou o relatório e o tipo inalterados
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    template_name = 'reports/relatorio_confirm_delete.html'
    success_url = reverse_lazy('reports:report_list')


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Report
    template_name = 'reports/relatorio_detail.html'
    context_object_name = 'report'

def export_report_pdf(request, pk):
    report = Report.objects.get(pk=pk)
    # Renderiza o template de detalhe, mas usando um CSS sem variáveis
    # Você pode inserir o CSS inline ou ler de um arquivo
    css_path = os.path.join(settings.BASE_DIR, 'static', 'css', 'pdf_style.css')
    with open(css_path, 'r', encoding='utf-8') as f:
        pdf_css = f.read()

    html = render_to_string('reports/relatorio_detail.html', {'report': report})
    # Insere o CSS inline dentro do HTML para o PDF
    full_html = f"<style>{pdf_css}</style>{html}"
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="report_{report.id}.pdf"'
    pisa_status = pisa.CreatePDF(full_html, dest=response)
    if pisa_status.err:
        return HttpResponse('Ocorreu um erro durante a criação do PDF <pre>' + html + '</pre>')
    return response


