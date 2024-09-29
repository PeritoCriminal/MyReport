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

VIEW CONCTACT, A DESENVOLVER


"""


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..forms import EditProfileForm

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Seu perfil foi atualizado com sucesso!')
            return redirect('edit_profile')  # Redireciona para a página de edição após salvar
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form,
        'aviso': 'Atualize seus dados abaixo',
        'recado': 'Preencha apenas os campos que deseja alterar.',
    }

    return render(request, 'account/edit_profile.html', context)
