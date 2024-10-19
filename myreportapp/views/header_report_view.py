from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from ..models.custom_user_model import UserRegistrationModel
from ..models.header_report_model import HeaderReportModel
# from datetime import datetime

@login_required(login_url='/login/')
def HeaderReportView(request, report_id=0):
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)
    msg_about_this_form_to_user = 'Formulário Para Edição de Novo Laudo.'
    
    id_report = report_id
    report = HeaderReportModel()
    if id_report:
        report = get_object_or_404(HeaderReportModel, id=id_report)

         # Verifica novamente se o usuário tem permissão para editar o relatório
        if report.reporting_expert != user:
            return HttpResponseForbidden("Você não tem permissão para editar este relatório.")

        msg_about_this_form_to_user = f'Atualização do Laudo {report.report_number}, RE {report.protocol_number}.'

    if request.method == 'POST':
        try:
            get_id_report = int(request.POST.get('id_report'))
        except:
            get_id_report = 0
           
        report = HeaderReportModel()
        if get_id_report > 0:
            report = HeaderReportModel.objects.get(id=int(get_id_report))

        print(get_id_report)
       
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
        report.protocol_number = request.POST.get('protocol')
        report.police_report_number = request.POST.get('police_report_number')
        report.examination_objective = request.POST.get('examination_objective')
        report.incident_nature = request.POST.get('incident_nature')
        report.police_station = request.POST.get('police_station')
        report.requesting_authority = request.POST.get('requesting_authority')
        report.expert_display_name = user_data.full_name
        report.institute_director = user_data.director
        report.institute_unit = user_data.unit
        report.forensic_team_base = user_data.team
        report.photographer = request.POST.get('photographer', '')
        report.considerations = request.POST.get('considerations', '')
        report.conclusion = request.POST.get('conclusion', '')
        report.save()

        return redirect('modules_report', report_id=report.id)

    context = {
        'msg_about_this_form_to_user': msg_about_this_form_to_user,
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

