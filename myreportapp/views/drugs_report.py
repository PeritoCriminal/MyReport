from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models.drugs_report_model import DrugReport
from ..models.custom_user_model import UserRegistrationModel
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError

@login_required(login_url='/login/')
def drugs_report(request):
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)

    if request.method == 'POST':
        # TESTE  -  Até agora dando Null para todos ... OU SEJA, OS VAORES DAS VARIÁEIS DO TEMPLATE NÃO ESTÃO CHEGANDO AQUI.
        # print('Protocol:', request.POST.get('protocol'))
        # print('Release Date:', request.POST.get('releaseDate'))
        # print('Service Hour:', request.POST.get('serviceHour'))


        try:
            materialImage = request.FILES.get('imgOfAllMaterialReceived')  # Obtém a imagem do formulário
            materialImageCaption = request.POST.get('labelOfImgOfAllMaterialReceived')

            new_report = DrugReport(
                report_number='000/00',
                protocol_number=request.POST.get('protocolo'),
                designated_date='2024-09-19',#request.POST.get('releaseDate'),
                exam_objective='Constatação Provisória',
                occurrence_nature='Entorpecente',
                occurring_number=request.POST.get('boletim'),
                police_station=request.POST.get('delegacia'),
                requesting_authority=request.POST.get('autoridade_requisitante'),
                activation_date=request.POST.get('data_atendimento'),
                activation_time=request.POST.get('hora_atendimento'),
                service_date=request.POST.get('data_liberacao'),
                service_time=request.POST.get('hora_liberacao'),
                director=user_data.director,
                nucleus=user_data.unit,
                team=user_data.team,
                reporting_expert=user.full_name,
                assistant_expert='Não se aplica',
                photographer='Não se aplica',
                draftsman='Não se aplica',
                allSubstances=request.POST.getlist('substance[]'),
                materialReceivedObservations=request.POST.get('allMaterialObservations'),

                materialImage=request.POST.get('imageGeneralBase64'),
                materialImageCaption=request.POST.get('labelOfImgOfAllMaterialReceived'),

                listOfEnvolvedPeople=request.POST.getlist('people_involved[]'),
                #listItensLabels=request.POST.getlist('item_header[]'), eliminar isso é inútl
                listOfPackagings=request.POST.getlist('packaging[]'),
                listOfMorphology=request.POST.getlist('morphology[]'),
                listOfGrossMass=[float(x) for x in request.POST.getlist('massa_bruta[]') if x],
                listOfLiquidMass=[float(x) for x in request.POST.getlist('massa_liquida[]') if x],
                listOfReturned=[x == 'on' for x in request.POST.getlist('devolvido[]')],
                listOfCounterProof=[x == 'on' for x in request.POST.getlist('contrapericia[]')],
                listOfEntranceSeal=request.POST.getlist('lacre_entrada[]'),
                listOfExitseal=request.POST.getlist('lacre_saida[]'),
                listOfpackagingAndMorphology=request.POST.getlist('packagingAndMorphologiObservations[]'),
                listOfResultOfExams=request.POST.getlist('resultOfExams[]'),
                examImages=request.POST.getlist('imageItemExaminatedBase64[]'),
                examImageCaptions=request.POST.getlist('labelOfImgItemExaminatedReceived[]'),                
                returnedItemsImage=request.POST.get('material-devolvidoBase64'),
                returnedItemsCaption=request.POST.get('material_devolvido_legenda'),
                counterProofImage=request.POST.get('contrapericia-imagemoBase64'),
                counterProofCaption=request.POST.get('contrapericia_legenda'),
                considerations = request.POST.get('considerations'),
                conclusion = request.POST.get('conclusao'),

            )

            # print(f'Verificar o que está no post: {request.POST}')
            new_report.save()

            num_images = len(new_report.examImages)

            return HttpResponse(f'Relatório criado com sucesso! Imagens dos itens examinados = {num_images}')
        except Exception as e:
            return HttpResponse(f'Erro ao criar relatório: {str(e)}')  # ESSE ERRO ESTÁ SENDO EXIBIDO

    now = datetime.now()

    minutes = (now.minute // 15) * 15
    rounded_time = now.replace(minute=minutes, second=0, microsecond=0)
    formatted_current_time = rounded_time.strftime('%H:%M')

    before_time = rounded_time - timedelta(hours=1.5)
    formatted_before_time = before_time.strftime('%H:%M')

    today_date = now.date()

    if before_time.day != now.day:
        before_date = today_date - timedelta(days=1)  
    else:
        before_date = today_date  

    msg_about_this_form_to_user = (
        f'{user_data.full_name},<br>Este formulário serve como uma alternativa '
        'caso o Sistema GDL não esteja disponível. Preencha todos os campos com atenção, '
        'verifique todos os dados cuidadosamente, salve o laudo em formato PDF e '
        'assine-o com seu certificado digital. Caso o laudo seja enviado à autoridade requisitante, '
        'ele deverá ser registrado oportunamente no Sistema GDL.'
    )

    packaging = {
        'Selecione uma opção': '',
        'Plástico com nó': 'invólucro(s) plástico(s) fechado(s) por nó encerrando',
        'Plástico com filme': 'invólucro(s) plástico(s) do tipo "filme" retorcido encerrando',
        'Plástico com zip': 'invólucro(s) plástico(s) fechado(s) por pressão (tipo "zip") encerrando',
        'Plástico com calor': 'invólucro(s) plástico(s) fechado(s) por aquecimento encerrando',
        'Plástico com alumínio': 'invólucro(s) constituído(s) por plástico e papel alumínio encerrando',
        'Fita adesiva': 'invólucro(s) constituído(s) por fita(s) adesiva(s) retorcida(s) encerrando',
        'Eppendorf': 'microtubo(s) plástico(s) do tipo "Eppendorf" dotado(s) de tampa própria encerrando',
        'Frasco vítreo': 'Frasco(s) vítreo(s) fechado(s) por batoque e tampa própria contendo',
        'Invólucro geral': 'invólucro(s) plástico(s) encerrando',
        'Outros': '[DESCREVA A EMBALAGEM]',
        'Apenas papel alumínio': 'invólucro(s) constituído(s) por papel alumínio encerrando',
        'Frasco com válvula (lança perfume)': 'Frasco(s) vítreos dotado(s) de válvula aspersora contendo',
        'Frasco plástico': 'Frasco(s) plástico(s) fechado(s) por tampa própria contendo',
        'Fita adesiva com plástico filme': 'invólucro(s) constituído(s) por fita(s) adesiva(s) e plástico(s) encerrando',
        'Garrafa pet': 'Garrafa(s) aparentemente do tipo PET, fechada(s) por tampa própria de rosca, contendo'
    }

    morphology = {
        'Selecione uma opção': '',
        'erva': 'porção de fragmentos vegetais ressequidos, constituídos de folhas, folíolos, inflorescências, caules e frutos.',
        'tijolo': 'contendo porção de fragmentos vegetais ressequidos, constituídos de folhas, folíolos, inflorescências, caules e frutos, compactados na forma de tijolo.',
        'planta': 'contendo planta arbustiva com [XX] cm de comprimento e constituído por raiz, caule, folhas, folíolos, inflorescência e frutos',
        'haxixe': 'contendo porção de substância de aspecto resinoso de coloração amarronzada e de morfologia irregular',
        'cigarro íntegro': 'contendo cigarro(s) artesanal(ais) confeccionado(s) em papel, contendo fragmentos vegetais ressequidos, constituídos de folhas, folíolos, inflorescências, caules e frutos.',
        'cigarro queimado': 'contendo cigarro(s) artesanal(ais) parcialmente queimado(s), confeccionado(s) em papel, contendo fragmentos vegetais ressequidos, constituídos de folhas, folíolos, inflorescências, caules e frutos.',
        'pó': 'contendo porção de material sólido particulado',
        'pedra': 'contendo porção de material sólido petrificado',
        'líquido': 'contendo fração líquida translúcida e volátil.',
        'resina': 'contendo porção de material resinoso',
        'comprimido': 'contendo porção de material particulado, compactado na forma de comprimido',
        'selo': 'contendo segmento de papel ilustrado, do tipo "picote" (selo).',
        'outros': '[Descreva a Morfologia]',
        'granulado': 'contendo porção de material sólido particulado com grânulos',
        'dichavador': 'contendo dichavador, do tipo triturador de rotação manual, da marca [X]/ sem marca aparente, de [material: madeira/metal/plástico/material sintético], composto por [X] partes, apresentado resquícios/sujidades.',
        'Semente/ fruto de maconha': 'contendo porção de material com aspecto de origem vegetal, de formato esférico, coloração amarronzada e com diâmetro médio de aproximadamente 3,0 mm (três milímetros).',
        'K4': 'contendo segmento(s) de papel de cor [descreva a cor]',
        'Liquidificador': 'contendo liquidificador, da marca [X]/ sem marca aparente, composto por base e recipiente com hélice de pás cortantes, apresentando resquícios/sujidades.',
        'balança': 'contendo balança, da marca [X]/ sem marca aparente, com mostrador digital, de carga máxima nominal de [X], apresentando resquícios/sujidades.',
        'faca': 'contendo faca, da marca [X]/ sem marca aparente, constituída por uma lâmina metálica cortante presa a um cabo de [material: madeira/metal/plástico], apresentando resquícios/sujidades.',
        'tesoura': 'contendo tesoura, da marca [X]/ sem marca aparente, constituída por duas lâminas metálicas cortantes, unidas por um eixo, apresentando resquícios/sujidades.',
        'embalagem plástica com resquícios': 'contendo embalagens plásticas com massa total de [X] gramas e resquícios do material [descrição do material].',
        'embalagem plástica': 'contendo embalagem plástica com massa total de [X] gramas e [descrição do material].'
    }
    exam_resulting = {  #FALTA IMPLENTAR OS TEXTOS DOS VALORES
        'cocaina': 'coca',
        'maconha': 'maconha',
        'crack': 'cocaina',
    }

    context = {
        'protocol_prefix': 'TOX',
        'delegacia': 'Del. Sec. Limeira Plantão',
        'lacre_saida': 'SPTC',
        'today_date': today_date,
        'current_time': formatted_current_time,
        'before_time': formatted_before_time,
        'before_date': before_date,
        'user_name': user.full_name,
        'msg_about_this_form_to_user': msg_about_this_form_to_user,
        'packaging': packaging,
        'morphology': morphology,
        'exam_resulting': exam_resulting,
    }
    
    return render(request, 'drugs_report.html', context)
