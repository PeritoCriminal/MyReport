from django import forms
#from .models import UserRegistrationModel
from ..models import UserRegistrationModel

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserRegistrationModel
        fields = ['full_name', 'city', 'unit', 'team', 'image']  # Inclua os campos que podem ser alterados
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
        }