from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime, timedelta

@login_required(login_url='/login/')
def drugs_report(request):
    now = datetime.now()

    # Dados de usuário
    user = request.user  # Isso está certo?
    
    # Arredondar current_time para o intervalo mais próximo de 15 minutos para baixo
    minutes = (now.minute // 15) * 15
    rounded_time = now.replace(minute=minutes, second=0, microsecond=0)
    formatted_current_time = rounded_time.strftime('%H:%M')
    
    # Subtrair uma hora e meia
    before_time = rounded_time - timedelta(hours=1.5)
    formatted_before_time = before_time.strftime('%H:%M')
    
    # Obter a data de hoje
    today_date = now.date()
    
    # Verificar se o horário anterior está em um dia anterior
    if before_time.day != now.day:
        before_date = today_date - timedelta(days=1)  # Se `before_time` for de um dia anterior
    else:
        before_date = today_date  # Se for do mesmo dia
    
    # Mensagem para o usuário
    msg_about_this_form_to_user = (
        f'{user.full_name},<br>Este formulário serve como uma alternativa '
        'caso o Sistema GDL não esteja disponível. Preencha todos os campos com atenção, '
        'verifique todos os dados cuidadosamente, salve o laudo em formato PDF e '
        'assine-o com seu certificado digital. Caso o laudo seja enviado à autoridade requisitante, '
        'ele deverá ser registrado oportunamente no Sistema GDL.'
    )

    packaging = {
    'Selecione uma opção':'',
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
    'Selecione uma opção':'',
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
    'embalagem plástica com resquícios': 'contendo embalagens plásticas com massa total de [x] grama(s), cada unidade dotada de dimensões aproximadas de [x] cm de comprimento por [x] cm de largura, apresentando resquícios/sujidades.',
    'rolo de plástico filme/papel alumínio/ fita adesiva': 'contendo rolo de [plástico filme / papel alumínio / fita adesiva], da marca [X]/ sem marca aparente, apresentando resquícios/sujidades.',
    'mochila/bolsa/mala': 'contendo [mochila / bolsa / mala], de [tecido / couro / material sintético / lona], constituída de [X] compartimentos, apresentando resquícios/sujidades.',
    'skunk': 'contendo porção de fragmentos vegetais não compactados e constituídos principalmente de inflorescências',
    'Pote com sujidades': 'contendo recipiente de [cerâmica, vidro, plástico, metal, louça] dotado de tampa própria, apresentando resquícios/sujidades.',
    'cachimbo': 'contendo cachimbo [opcional: artesanal], de [material: madeira, barro, metal], constituído por um tubo delgado, apresentando fornilho em uma de suas extremidades contendo resquícios/sujidades.',
    'Frutos maconha': 'contendo frutos do tipo aquênio, ovalados, medindo cerca de 3 mm (três milímetros) de largura por 5 mm (cinco milímetros) de comprimento, com casca brilhante, dura e finamente reticulada.',
    'prato': 'contendo prato de [material: vidro, plástico, metal, louça], de formato [circular, quadrado], do tipo [raso, fundo] apresentando resquícios/sujidades.',
    'peneira': 'contendo peneira de formato circular, dotada de cabo e trama [material: metálicos, de plástico], apresentando resquícios/sujidades.'
    }

    exam_resulting = {
        'Selecione uma opção': '',
        'negativo': 'NÃO FOI POSSÍVEL IDENTIFICAR presença de substâncias elencadas nas listas A, B e F da Portaria SVS/MS 344/98 e atualizações posteriores, ou na Portaria MJSP 204/2022, em sua lista III, conforme a(s) técnica(s) utilizada(s) (Portaria SPTC 42/2024)',
        'inconclusivo': 'Os exames/análises preliminares mostraram-se INCONCLUSIVOS, sendo necessárias análises mais complexas e morosas, incompatíveis com a rapidez demandada pelos exames de constatação. O resultado deste presente item seguirá em laudo definitivo.',
        'cocaína': 'foi DETECTADA presença da substância COCAÍNA, constante na lista F1 da Portaria SVS/MS 344/98 e atualizações posteriores',
        'thc': 'foi DETECTADA presença da substância TETRAHIDROCANNABINOL (THC), constante na lista F2 da Portaria SVS/MS 344/98 e atualizações posteriores'
    }
    
    # Contexto para renderizar o template
    context = {
        'protocol_prefix': 'TOX',
        'delegacia': 'Del. Sec. Limeira Plantão',
        'today_date': today_date,
        'current_time': formatted_current_time,
        'before_time': formatted_before_time,
        'before_date': before_date,  # Adicionando before_date ao contexto
        'user_name': user.full_name,
        'msg_about_this_form_to_user': msg_about_this_form_to_user,
        'packaging': packaging,
        'morphology': morphology,
        'exam_resulting': exam_resulting,
    }
    
    return render(request, 'drugs_report.html', context)
