from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def reports(request):
    # Dados das imagens e seus respectivos links
    report_links = [
        {
            'url': 'drugs_report',
            'image': 'images/reports_links/drugs.jpg',
            'alt': 'Relatório de Drogas',
            'title': 'Entorpecentes - Constatação Provisória',
        },
        # Adicionar outras imagens e links
    ]
    return render(request, 'reports.html', {'report_links': report_links})
