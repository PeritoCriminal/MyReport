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

MODEL PARA USUÁRIO


"""

from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser

class UserRegistrationModel(AbstractUser):
    director = models.CharField(
        max_length=255, 
        default='Dr. José Carlos de Freitas Garcia Caldas',
        help_text='Inclua do atual Diretor, incluindo Dr. ou Dra.',
        )
    full_name = models.CharField(
        'Nome Completo', 
        max_length=100, 
        default='',
        help_text='Inclua o nome como deseja que apareça no laudo, incluindo Dr. ou Dra.'
    )
    city = models.CharField(
        'Cidade', 
        max_length=100, 
        default='Limeira'
    )
    unit = models.CharField(
        'Núcleo', 
        max_length=100, 
        default='Núcleo de Americana'
    )
    team = models.CharField(
        'Equipe', 
        max_length=100, 
        default='EPC - Limeira'
    )
    image = StdImageField(
        'Imagem',
        upload_to='user_images/',
        null=True, 
        blank=True,
        variations={'thumbnail': (100, 100)}
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        permissions = [
            ("can_view_custom_user", "Can view custom user"),
        ]

    # Define related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='Groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

