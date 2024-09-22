from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models.drugs_report_model import DrugReport
from ..models.custom_user_model import UserRegistrationModel
from datetime import datetime, timedelta
from docx import Document
from io import BytesIO

@login_required(login_url='/login/')
def drugs_report(request):
    user = request.user
    user_data = UserRegistrationModel.objects.get(username=user.username)

    if request.method == 'POST':        
        try:            
            new_report = DrugReport(
                report_number='000/00',
                city=user_data.city,
                protocol_number=request.POST.get('protocolo'),
                designated_date=request.POST.get('data_atendimento'),
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
                listOfPackagings=request.POST.getlist('packaging[]'),
                listOfMorphology=request.POST.getlist('morphology[]'),
                listOfGrossMass=[float(x) for x in request.POST.getlist('massa_bruta[]') if x],
                listOfLiquidMass=[float(x) for x in request.POST.getlist('massa_liquida[]') if x],
                listOfReturned=request.POST.get('listOfReturndCheckBoxes'),
                listOfCounterProof=request.POST.get('listOfCounterproofCheckBoxes'),
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
            new_report.save()

            doc = Document()

            # Gera o preâmbulo usando o método do model
            preamble_text = new_report.generate_preamble()
    
            # Adiciona o preâmbulo ao documento
            doc.add_paragraph(preamble_text)

            # Adiciona título e conteúdo ao documento
            doc.add_heading('Relatório de Exame de Drogas', 0)
            doc.add_paragraph(f'Número do Relatório: {new_report.report_number}')
            doc.add_paragraph(f'Protocolo: {new_report.protocol_number}')
            doc.add_paragraph(f'Data de Designação: {new_report.designated_date}')
            # Adicione outros campos conforme necessário

            # Salva o documento em um buffer de memória
            doc_buffer = BytesIO()
            doc.save(doc_buffer)
            doc_buffer.seek(0)

            response = HttpResponse(doc_buffer, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=Relatorio_Drogas.docx'
            
            return response
            #return HttpResponse(f'Relatório criado com sucesso!')
        except Exception as e:
            return HttpResponse(f'Erro ao criar relatório: {str(e)}')
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
        'Selecione uma opção': '',
        'Negativo': 'NÃO FOI POSSÍVEL IDENTIFICAR presença de substâncias elencadas nas listas A, B e F da Portaria SVS/MS 344/98 e atualizações posteriores, ou na Portaria MJSP 204/2022, em sua lista III, conforme a(s) técnica(s) utilizada(s) (Portaria SPTC 42/2024).',
        'Inconclusivo': 'Os exames/análises preliminares mostraram-se INCONCLUSIVOS, sendo necessárias análises mais complexas e morosas, incompatíveis com a rapidez demandada pelos exames de constatação. O resultado deste presente item seguirá em laudo definitivo.',
        'Cocaina': 'foi DETECTADA presença da substância COCAÍNA, constante na lista F1 da Portaria SVS/MS 344/98 e atualizações posteriores',
        'Maconha': 'foi DETECTADA presença da substância TETRAHIDROCANNABINOL (THC), constante na lista F2 da Portaria SVS/MS 344/98 e atualizações posteriores',
        }
    
    conterproof_returndmaterial = {
        'ff':'todo o material disponível foi utilizado nas análises do presente Laudo. Face a sua exiguidade não foi possível armazenar amostra de contraperícia.',
        'fv':'todo o material foi aqui retirado para análises, sendo o remanescente destas análises armazenado sob a forma de contraperícia.',
        'vv':'uma amostra de aproximadamente 2 g (dois gramas) foi aqui retirada para análises, sendo o remanescente destas análises armazenado sob a forma de contraperícia.'
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
        'conterproof_returndmaterial': conterproof_returndmaterial,
        'alert': '(Este Laudo é de caráter provisório e não confirma necessariamente o resultado da identificação que será enviado no Laudo Definitivo)',
    } 

    return render(request, 'drugs_report.html', context)

# Devo criar meu docx aqui?
