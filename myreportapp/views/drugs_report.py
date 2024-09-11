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
    }
    
    return render(request, 'drugs_report.html', context)
