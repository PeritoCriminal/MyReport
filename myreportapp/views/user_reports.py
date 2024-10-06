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

VIEW CONCTACT, A DESENVOLVER


"""


from django.shortcuts import render

from ..models.theft_report_model import TheftReportModel

def userReports(request):
    user = request.user
    local_reports = TheftReportModel.objects.filter(reporting_expert=user.full_name)

    context = {
        'local_reports': local_reports,
    }

    return render(request, 'user_reports.html', context)