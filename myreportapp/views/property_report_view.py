from django.shortcuts import render, get_object_or_404, redirect
from ..models import ScenePreservationReportModel, HeaderReportModel, PropertyReportModel
from django.contrib.auth.decorators import login_required

@login_required
def PropertyReportView(request, report_id):
    # Obtém o cabeçalho do relatório associado ao usuário logado
    report = get_object_or_404(HeaderReportModel, id=report_id, reporting_expert=request.user)

    # Inicialmente tenta buscar o relatório de preservação, se ele existir
    try:
        # Verifica se já existe um relatório de imóvel vinculado ao cabeçalho
        property = PropertyReportModel.objects.get(reportForeignKey=report)
        print(f'Valor da chave estrangeira = {property.reportForeignKey}, id = {report.id}')
    except PropertyReportModel.DoesNotExist:
        # Se não existir, inicializa como None para criar depois
        property = None
        print(f'não há ainda descrição de imóvel para o laudo {report.id}')

    # Se o método for POST, significa que o formulário foi enviado
    if request.method == 'POST':
        property_description = request.POST.get('property')

        # Divide o texto em parágrafos (usando \n como delimitador) e remove parágrafos vazios
        paragraphs = [p.strip() for p in property_description.split('\n') if p.strip()]

        if property:
            # Se o relatório já existir, atualiza os dados existentes
            property.description = '\n'.join(paragraphs)  # Salva os parágrafos unidos
        else:
            # Se não existir, cria um novo registro
            property = PropertyReportModel(
                reportForeignKey=report,
                description='\n'.join(paragraphs)  # Salva os parágrafos unidos
            )
        
        # Salva o relatório (seja criação ou atualização)
        property.save()

        # Redireciona para a página desejada após o salvamento
        return redirect('modules_report', report.id)  # Ajuste o nome da view de destino

    # Se for uma requisição GET (ou outra), renderiza o formulário
    context = {
        'report': report,
        'property': property,
        'msg': 'Preencha o formulário de propriedade.',
    }

    return render(request, 'propertyreport.html', context)