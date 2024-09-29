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

FORM PARA CONFIGURAÇÕES DO USUÁRIO
"""



from django import forms
from django.contrib.auth.forms import PasswordChangeForm  # Importa o formulário de alteração de senha
from ..models import UserRegistrationModel

class EditProfileForm(forms.ModelForm):
    new_password = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput,
        required=False,  # Senha não é obrigatória, a menos que o usuário queira alterá-la
    )
    confirm_password = forms.CharField(
        label='Confirmar Senha',
        widget=forms.PasswordInput,
        required=False,  # Senha não é obrigatória
    )

    class Meta:
        model = UserRegistrationModel
        fields = ['full_name', 'city', 'unit', 'team', 'image', 'new_password', 'confirm_password']  # Inclua os novos campos
        labels = {
            'full_name': 'Nome Completo',
            'city': 'Cidade',
            'unit': 'Núcleo',
            'team': 'Equipe',
            'image': 'Imagem',
        }
        help_texts = {
            'full_name': 'Inclua o nome como deseja que apareça no laudo, incluindo Dr. ou Dra.',
            'image': 'Envie uma imagem para o perfil. Formato suportado: JPEG, PNG.',
            'new_password': 'Deixe em branco se não quiser alterar a senha.',
            'confirm_password': 'Deixe em branco se não quiser alterar a senha.',
        }
