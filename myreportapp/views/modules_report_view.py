from django.shortcuts import render, get_object_or_404
from ..models.header_report_model import HeaderReportModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def ModulesReportView(request, report_id):
    # Verifica se o relatório existe e se pertence ao usuário
    report = get_object_or_404(HeaderReportModel, id=report_id, reporting_expert=request.user)

    context = {
        'report': report,
    }

    return render(request, 'modulesreport.html', context)
