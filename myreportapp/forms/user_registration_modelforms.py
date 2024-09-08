from django import forms
from ..models.custom_user_model import UserRegistrationModel
from django.utils.translation import gettext_lazy as _

class UserRegistrationModelForm(forms.ModelForm):

    email = forms.EmailField(
        initial='@policiacientifica.sp.gov.br',
        required=True,
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seu email @policiacientifica.sp.gov.br',
        })
    )

    password1 = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        help_text=_('Sua senha deve ter pelo menos 8 caracteres e incluir letras e números.')
    )
    
    password2 = forms.CharField(
        label=_("Confirme a senha"),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'}),
        help_text=_('Digite a mesma senha novamente para confirmação.')
    )

    class Meta:
        model = UserRegistrationModel
        fields = ['director', 'username', 'full_name', 'email', 'city', 'unit', 'team', 'image']
        labels = {
            'director': _('Direitor do Instituto de Criminalítica de SP'),
            'username': _('Usuário'),
            'full_name': _('Nome Completo'),
            'email': _('E-mail'),
            'city': _('Cidade'),
            'unit': _('Núcleo'),
            'team': _('Equipe'),
            'image': _('Imagem do Perito'),
        }
        help_texts = {
            'full_name': _('Inclua seu nome da forma como deseja que apareça no laudo, incluindo Dr. ou Dra., conforme o caso.'),       
        }
        widgets = {
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', _('As senhas não coincidem.'))

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        
        # Print the user object before saving
        print("User object before save:", {
            'username': user.username,
            'full_name': user.get_full_name(),
            'email': user.email,
            'city': user.city,
            'unit': user.unit,
            'team': user.team,
            'image': user.image,
            'password': '********'  # Do not print actual password
        })

        if commit:
            user.save()
        return user
