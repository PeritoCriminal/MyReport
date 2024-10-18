from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.custom_user_model import UserRegistrationModel
from ..models.header_report_model import HeaderReportModel
from datetime import datetime

from datetime import datetime

@login_required(login_url='/login/')
def HeaderImportView(request, report_id=None):
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)

    # Recuperar ou criar um novo relatório
    if report_id:
        report = get_object_or_404(HeaderReportModel, id=report_id)
        print('Atualização de Relatório')
    else:
        print('Novo relatório')
        report = HeaderReportModel()





    if request.method == 'POST':
        # Tenta obter o id_report do formulário
        id_report = request.POST.get('id_report')

        try:
            # Verifica se o id_report é válido (número e não vazio)
            if id_report and id_report.isdigit():
                # Busca o relatório existente pelo ID
                report = HeaderReportModel.objects.get(id=id_report)
            else:
                # Se id_report for None ou inválido, cria um novo relatório
                report = HeaderReportModel()
        except HeaderReportModel.DoesNotExist:
            # Caso o relatório com o id não exista, cria um novo relatório
            report = HeaderReportModel()






        # daqui para baixo vai preencher os dados.    
        report.report_date = '2024-10-10'  # Substitua pela data atual quando necessário
        report.designation_date = request.POST.get('designated_date')
        report.occurrence_date = request.POST.get('occurrence_date')
        report.occurrence_time = request.POST.get('occurrence_time')
        report.activation_date = request.POST.get('call_date')
        report.activation_time = request.POST.get('call_time')
        report.service_date = request.POST.get('service_date')
        report.service_time = request.POST.get('service_time')
        report.report_number = request.POST.get('report_number')
        report.city = user_data.city
        report.protocol_number = request.POST.get('protocolo')
        report.police_report_number = request.POST.get('police_report_number')
        report.examination_objective = request.POST.get('examination_objective')
        report.incident_nature = request.POST.get('incident_nature')
        report.police_station = request.POST.get('police_station')
        report.requesting_authority = request.POST.get('requesting_authority')
        report.institute_director = user_data.director
        report.institute_unit = user_data.unit
        report.forensic_team_base = user_data.team
        report.photographer = request.POST.get('photographer', '')
        report.considerations = request.POST.get('considerations', '')
        report.conclusion = request.POST.get('conclusion', '')

        # Salvar as mudanças (para atualização ou criação de um novo relatório)
        report.save()

    context = {
        'msg_about_this_form_to_user': 'Laudo Técnico Pericial',
        'designated_date': report.dateToForm(report.designation_date),
        'occurrence_date': report.dateToForm(report.occurrence_date),
        'occurrence_time': report.hourToForm(report.occurrence_time),
        'activation_date': report.dateToForm(report.activation_date),
        'activation_time': report.hourToForm(report.activation_time),
        'service_date': report.dateToForm(report.service_date),
        'service_time': report.hourToForm(report.service_time),
        'report': report,
        'user_data': user_data,
    }

    return render(request, 'headerreport.html', context)

