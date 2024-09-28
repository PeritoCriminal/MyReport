"""

Copyright (c) 2024 Marcos de Oliveira Capristo
Todos os direitos reservados.

MYREPORT é um projeto independente.
Oferece um ambiente para edição de laudos periciais,
voltado especialmente para Peritos Criminais Oficiais do Estado de São Paulo.
Idealizado e inicialmente desenvolvido pelo Perito Criminal Marcos de Oliveira Capristo.
Contato: marcos.moc@policiacientifica.sp.gov.br | (19) 9 8231-2774


"""

"""

VIEW REPORTS, DESENVOLVIMENTO PARADO, A VIEW DROGS_REPORT


"""



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
