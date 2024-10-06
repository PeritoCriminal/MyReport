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

MODEL PARA LAUDO DE LOCAL DE FURTO

"""


from django.db import models
from .base_report_model import BaseReport

class TheftReportModel(BaseReport):
    preservation_context = models.TextField(blank=True, verbose_name='Preservação', default='')
    localsubtitle = models.JSONField(blank=True, verbose_name='Subtítulo', default=list)
    localdescription = models.JSONField(blank=True, verbose_name='Descrição', default=list)
    localimgbase64 = models.JSONField(blank=True, verbose_name='Imagem Base 64', default=list)
    locallegend = models.JSONField(blank=True, verbose_name='Legenda da Imagem', default=list)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Local de Furto'
        verbose_name_plural = 'Locais de Furto'
