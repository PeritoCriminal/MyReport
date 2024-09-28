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

VIEW REGISTE, A MELHORAR


"""



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from ..forms.user_registration_model import UserRegistrationModelForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationModelForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('reports')
        else:
            messages.error(request, 'Erro ao criar conta. Verifique os dados e tente novamente.')
    else:
        form = UserRegistrationModelForm()

    # Mensagem adicional para senha
    msg_simple_password = 'IMPORTANTE. Utilize uma senha simples, fácil de lembrar, anote se necessário. Por enquanto não há um serviço de recuperação de senhas.'

    # Mesangem para registrar o nome do diretor do IC
    msg_simple_director = 'O nome do atual direitor do IC deve verificado. Altere se necessário. Inclua Dr. ou Dra. antes do nome para que o texto do preâmbulo seja gerado corretamente.'

    director = 'Dr. José Carlos de Freitas Garcia Caldas' # Direitor do Instituto de Criminalística de São Paulo em 2024
    
    context = {
        'form': form,
        'msg_simple_password': msg_simple_password,
        'msg_simple_director': msg_simple_director,
        'director': director,
    }
    
    return render(request, 'account/register.html', context)

