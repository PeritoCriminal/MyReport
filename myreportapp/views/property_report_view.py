from django.shortcuts import render, get_object_or_404, redirect
from ..models import ScenePreservationReportModel, HeaderReportModel, PropertyReportModel
from django.contrib.auth.decorators import login_required

@login_required
def PropertyReportView(request, report_id):
    report = get_object_or_404(HeaderReportModel, id=report_id, reporting_expert=request.user)

    try:
        property = PropertyReportModel.objects.get(reportForeignKey=report)
    except PropertyReportModel.DoesNotExist:
        property = None

    if request.method == 'POST':
        # property_title = request.POST.get('title')
        property_subtitle = request.POST.get('subtitle')
        property_description = request.POST.get('property')
        property_image = request.FILES.get('image')
        property_legend = request.POST.get('legend')

        paragraphs = [p.strip() for p in property_description.split('\n') if p.strip()]

        if property:
            # property.title = property_title  # Atualiza o título
            property.subtitle = property_subtitle  # Atualiza o subtítulo
            property.description = '\n'.join(paragraphs)  # Atualiza a descrição
            property.legend = property_legend
            if property_image:  # Atualiza a imagem se uma nova foi enviada
                property.image = property_image
        else:
            property = PropertyReportModel(
                reportForeignKey=report,
                #title=property_title,  # Salva o título
                subtitle=property_subtitle,  # Salva o subtítulo
                description='\n'.join(paragraphs),  # Salva a descrição
                image=property_image, # Salva a imagem se fornecida
                legend=property_legend,
            )
        
        property.save()
        return redirect('modules_report', report.id)
    
    img_name = property.image.name if property and property.image else 'Nenhum arquivo selecionado'


    context = {
        'report': report,
        'property': property,
        'img_name': img_name,
        'msg': 'Preencha o formulário de propriedade.',
    }

    return render(request, 'propertyreport.html', context)