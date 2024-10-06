from django.shortcuts import get_object_or_404, redirect
from ..models import TheftReportModel

def deleteReport(request, report_id):
    report = get_object_or_404(TheftReportModel, id=report_id)
    report.delete()
    return redirect('user_reports')  # Redireciona para a lista de laudos após deletar
