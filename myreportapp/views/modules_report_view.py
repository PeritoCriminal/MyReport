from django.shortcuts import render, get_object_or_404
from ..models import HeaderReportModel, ScenePreservationReportModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def ModulesReportView(request, report_id):
    # Verifica se o relatório existe e se pertence ao usuário
    report = get_object_or_404(HeaderReportModel, id=report_id, reporting_expert=request.user)
    scene_preservation = get_object_or_404(ScenePreservationReportModel, reportForeignKey=report)

    context = {
        'report': report,
        'scene_preservation': scene_preservation,
        'occurrence_date': report.dateToDoc(report.occurrence_date),
        'occurrence_time': report.hourToDoc(report.occurrence_time),
        'activation_date': report.dateToDoc(report.activation_date),
        'activation_time': report.hourToDoc(report.activation_time),
        'service_date': report.dateToDoc(report.service_date),
        'service_time': report.hourToDoc(report.service_time),
    }

    return render(request, 'modulesreport.html', context)
