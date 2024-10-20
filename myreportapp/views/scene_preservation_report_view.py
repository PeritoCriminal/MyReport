from django.shortcuts import render, get_object_or_404
from ..models.scene_preservation_report_model import ScenePreservationReportModel, HeaderReportModel
from django.contrib.auth.decorators import login_required

@login_required
def ScenePreservationReportView(request, report_id):

    report = get_object_or_404(HeaderReportModel, id=report_id, reporting_expert=request.user)

    context = {
        'report': report,
        'msg': 'Mensagem ao usuário',
    }
    return render(request, 'scenepreservationreport.html', context)