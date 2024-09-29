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

VIEW PARA CONFIGURAÇÕES DO USUÁRIO

"""



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash  # Importa a função para atualizar a sessão
from ..forms import EditProfileForm

@login_required
def editProfile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        
        # Obtenha a nova senha e a confirmação da senha do formulário
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if form.is_valid():
            form.save()  # Salva as alterações no perfil

            # Verifica se o usuário deseja alterar a senha
            if new_password and new_password == confirm_password:
                request.user.set_password(new_password)  # Altera a senha do usuário
                request.user.save()  # Salva o usuário com a nova senha
                update_session_auth_hash(request, request.user)  # Mantém o usuário logado após a alteração da senha
                messages.success(request, 'Seu perfil foi atualizado com sucesso e a senha foi alterada!')
            else:
                messages.error(request, 'As senhas não correspondem ou estão vazias.')

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
