from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models.custom_user_model import UserRegistrationModel
from ..models.header_report_model import HeaderReportModel

@login_required(login_url='/login/')
def HeaderImportView(request, report_id=None):  # display como cofiguro a view e o urls para recuperar um registro e enviar os dados ao formulário?
    
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)

    if report_id:
        report = get_object_or_404(HeaderReportModel, id=report_id)
        print('Atualização de Relatório')
    else:
        print('Novo relatório')

    if request.method == 'POST':
        print('Agora, Método POST')

    context = {
        'msg_about_this_form_to_user': 'Laudo Téncio Pericial',
        'designated_date': '1900-01-01',
        'report_number': 'Número do Laudo',
        'protocol_number': 'Número do Protocolo',
        'occurrence_date': '1900-01-01',
        'occurrence_time': '00:00:00',
        'call_date': '1900-01-01',
        'call_time': '00:00:00',
        'service_date': '1900-01-01',
        'service_time': '00:00:00',
        'police_report_number': 'Número do Boletim',
        'police_station': 'Delegacia',
        'requesting_authority': 'Autoridade Requisitante',
        'examination_objective': 'Objetivo do Exame',
        'incident_nature': 'Natureza da Ocorrência',
    }


    return render(request, 'headerreport.html', context)