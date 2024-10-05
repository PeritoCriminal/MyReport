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


from django.shortcuts import render

from ..models.custom_user_model import UserRegistrationModel
from ..models.theft_report_model import TheftReportModel


def theft(request):
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)

    if request.method == 'POST':

        try:
            newReport = TheftReportModel(
                report_number=request.POST.get('laudo'),
                city=user_data.city,
                protocol_number=request.POST.get('protocolo'),
                designated_date='14-05-2024',
                exam_objective='constatação de furto',
                occurrence_nature='exame inicial',
                occurring_number=request.POST.get('boletim'),
                police_station=request.POST.get('delegacia'),
                requesting_authority=request.POST.get('autoridade_requisitante'),
                activation_date='14-05-2024',
                activation_time=request.POST.get('hora_atendimento'),
                service_date='14-05-2024',
                service_time=request.POST.get('hora_liberacao'),
                director=user_data.director,
                nucleus=user_data.unit,
                team=user_data.team,
                reporting_expert=user.full_name,
                assistant_expert='Não se aplica',
                photographer=request.POST.get('fotografo'),
                draftsman='Não se aplica',
            )
        except Exception as e:
            print(f'Erro: {e}')

        reportNumber = request.POST.get('laudo')

        if reportNumber:
            print("Relatório criado com sucesso:")
            for field, value in newReport.__dict__.items():
                print(f'{field}: {value}')
        else:
            print("POST request falhou. Nenhum número de laudo foi recebido.")

    context = {
        'user_data': user_data,
        'msg_about_this_form_to_user': 'Editor Laudo',
    }

    return render(request, 'furto.html', context)
