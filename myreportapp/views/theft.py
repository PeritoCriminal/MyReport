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

VIEW FURTO, A DESENVOLVER


"""


from django.shortcuts import render, redirect, get_object_or_404
from ..models.custom_user_model import UserRegistrationModel
from ..models.theft_report_model import TheftReportModel

def theft(request, report_id=None):
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)
    message = None
    numberOfLocals = 0
    list_local_subtitle = []
    new_report = True
    
    # Verificar se o relatório já existe (edição) ou se será um novo
    if report_id:
        report = get_object_or_404(TheftReportModel, id=report_id)  # Busca o relatório existente para edição
        numberOfLocals = len(report.localsubtitle)  # Calcula o número de locais
        list_local_subtitle = report.localsubtitle  # Passa a lista de subtítulos locais
        new_report = False
    else:
        report = None  # Criação de novo relatório

    if request.method == 'POST':
        try:
            # Se for uma edição de relatório existente
            if not new_report:
                report.report_number = request.POST.get('laudo')
                report.protocol_number = request.POST.get('protocolo')
                report.designated_date = request.POST.get('data_designacao')
                report.exam_objective = request.POST.get('objetivo')
                report.occurrence_nature = request.POST.get('naturesa')
                report.occurring_number = request.POST.get('boletim')
                report.police_station = request.POST.get('delegacia')
                report.requesting_authority = request.POST.get('autoridade_requisitante')
                report.activation_date = request.POST.get('data_acionamento')
                report.activation_time = request.POST.get('hora_atendimento')
                report.service_date = request.POST.get('data_atendimento')
                report.service_time = request.POST.get('hora_atendimento')
                report.photographer = request.POST.get('fotografo')
                report.preservation_context = request.POST.get('preservationContext')
                report.localsubtitle = request.POST.getlist('local-subtitle[]')
                report.localdescription = request.POST.getlist('local-description[]')
                report.localimgbase64 = request.POST.getlist('local-img-to-text-base64[]')
                report.locallegend = request.POST.getlist('label-local-img[]')
                report.considerations = request.POST.get('considerations')
                report.conclusion = request.POST.get('conclusions')
                report.save()  # Salva o relatório editado
                message = "Relatório atualizado com sucesso!"
            
            # Se não for uma edição, cria um novo relatório
            else:
                newReport = TheftReportModel(
                    report_number=request.POST.get('laudo'),
                    city=user_data.city,
                    protocol_number=request.POST.get('protocolo'),
                    designated_date=request.POST.get('data_designacao'),
                    exam_objective=request.POST.get('objetivo'),
                    occurrence_nature=request.POST.get('naturesa'),
                    occurring_number=request.POST.get('boletim'),
                    police_station=request.POST.get('delegacia'),
                    requesting_authority=request.POST.get('autoridade_requisitante'),
                    activation_date=request.POST.get('data_acionamento'),
                    activation_time=request.POST.get('hora_atendimento'),
                    service_date=request.POST.get('data_atendimento'),
                    service_time=request.POST.get('hora_atendimento'),
                    director=user_data.director,
                    nucleus=user_data.unit,
                    team=user_data.team,
                    reporting_expert=user.full_name,
                    assistant_expert='Não se aplica',
                    photographer=request.POST.get('fotografo'),
                    draftsman='Não se aplica',
                    preservation_context=request.POST.get('preservationContext'),
                    localsubtitle=request.POST.getlist('local-subtitle[]'),
                    localdescription=request.POST.getlist('local-description[]'),
                    localimgbase64=request.POST.getlist('local-img-to-text-base64[]'),
                    locallegend=request.POST.getlist('label-local-img[]'),
                    considerations=request.POST.get('considerations'),
                    conclusion=request.POST.get('conclusions'),
                )
                newReport.save()  # Salva o novo relatório
                message = "Relatório salvo com sucesso!"

            # return redirect('user_reports')

        except Exception as e:
            print(f'Erro: {e}')
            message = f"Erro ao salvar o relatório: {e}"

    context = {
        'list_local_subtitle': list_local_subtitle,
        'number_of_locals': numberOfLocals,
        'user_data': user_data,
        'report': report,
        'msg_about_this_form_to_user': 'Editor Laudo',
        'message': message,
    }

    return render(request, 'furto.html', context)
