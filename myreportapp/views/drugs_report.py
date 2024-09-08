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
    
    # Subtrair uma hora
    before_time = rounded_time - timedelta(hours=1.5)
    formatted_before_time = before_time.strftime('%H:%M')
    msg_about_this_form_to_user = f'{user.full_name},<br>Este formulário serve como uma alternativa caso o Sistema GDL não esteja disponível. Preencha todos os campos com atenção, verifique todos os dados cuidadosamente, salve o laudo em formato PDF e assine-o com seu certificado digital. Caso o laudo seja enviado à autoridade requisitante, ele deverá ser registrado oportunamente no Sistema GDL.'
    
    today_date = now.date()
    
    context = {
        'delegacia': 'Del. Sec. Limeira Plantão',
        'today_date': today_date,
        'current_time': formatted_current_time,
        'before_time': formatted_before_time,
        'user_name': user.full_name,
        'msg_about_this_form_to_user': msg_about_this_form_to_user,
    }
    return render(request, 'drugs_report.html', context)
