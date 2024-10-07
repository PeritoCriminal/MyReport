from django.shortcuts import render, get_object_or_404, redirect
from ..models.theft_report_model import TheftReportModel

def editReport(request, report_id):
    # Obter o relatório pelo ID
    report = get_object_or_404(TheftReportModel, id=report_id)

    number_of_items = len(report.localsubtitle) if report.localsubtitle else 0

    if request.method == 'POST':
        try:
            # Atualizando os dados do relatório com os dados enviados via POST
            report.report_number = request.POST.get('laudo')
            report.protocol_number = request.POST.get('protocolo')
            report.designated_date = request.POST.get('data_designacao')
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

            # Salvando o relatório atualizado
            report.save()

            # Redireciona para a página de "Meus Laudos" após salvar
            return redirect('user_reports')
        except Exception as e:
            print(f'Erro ao atualizar o relatório: {e}')
            message = f"Erro ao atualizar o relatório: {e}"
    else:
        message = None

    context = {
        'number_of_items': number_of_items,
        'report': report,  # Passa os dados do relatório para preencher o formulário
        'message': message,  # Exibe a mensagem, se houver
    }

    return render(request, 'edit_report.html', context)
