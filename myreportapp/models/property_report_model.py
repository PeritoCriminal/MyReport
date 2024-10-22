from django.db import models
from ..models import HeaderReportModel

class PropertyReportModel(models.Model):
    description = models.TextField(blank=True, verbose_name='Imóvel - Descrição', default='')
    reportForeignKey = models.ForeignKey(
        HeaderReportModel, 
        on_delete=models.CASCADE,  
        related_name='property',  
        verbose_name='Relatório Principal'
    )

    class Meta:
        verbose_name = 'Imóvel'