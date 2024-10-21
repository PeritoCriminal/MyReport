from django.shortcuts import render, get_object_or_404, redirect
from ..models.scene_preservation_report_model import ScenePreservationReportModel, HeaderReportModel
from django.contrib.auth.decorators import login_required

@login_required
def ScenePreservationReportView(request, report_id):
    # Obtém o cabeçalho do relatório associado ao usuário logado
    report = get_object_or_404(HeaderReportModel, id=report_id, reporting_expert=request.user)

    # Inicialmente tenta buscar o relatório de preservação, se ele existir
    try:
        # Verifica se já existe um relatório de preservação vinculado ao cabeçalho
        scene_preservation = ScenePreservationReportModel.objects.get(reportForeignKey=report)
        print(f'Valor da chave estrangeira = {scene_preservation.reportForeignKey}, id = {report.id}')
    except ScenePreservationReportModel.DoesNotExist:
        # Se não existir, inicializa como None para criar depois
        scene_preservation = None
        print(f'não há ainda descrição de preservação de local para o laudo {report.id}')

    # Se o método for POST, significa que o formulário foi enviado
    if request.method == 'POST':
        if scene_preservation:
            # Se o relatório já existir, atualiza os dados existentes
            scene_preservation.description = request.POST.get('preservation')
        else:
            # Se não existir, cria um novo registro
            scene_preservation = ScenePreservationReportModel(
                reportForeignKey=report,
                description=request.POST.get('preservation')
            )
        
        # Salva o relatório (seja criação ou atualização)
        scene_preservation.save()

        # Redireciona para a página desejada após o salvamento
        return redirect('modules_report', report.id)  # Ajuste o nome da view de destino

    # Se for uma requisição GET (ou outra), renderiza o formulário
    context = {
        'report': report,
        'scene_preservation': scene_preservation,
        'msg': 'Preencha o formulário de preservação da cena.',
    }

    return render(request, 'scenepreservationreport.html', context)

