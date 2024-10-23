from django.db import models
from ..models import HeaderReportModel

class PropertyReportModel(models.Model):
    title = models.CharField(max_length=200, blank=True, default='')
    subtitle = models.CharField(max_length=200, blank=True, default='')
    description = models.TextField(blank=True, verbose_name='Imóvel - Descrição', default='')
    image = models.ImageField(blank=True, null=True, upload_to='property_images/', default='')
    legend = models.CharField(max_length=200, blank=True, default='')
    reportForeignKey = models.ForeignKey(
        HeaderReportModel, 
        on_delete=models.CASCADE,  
        related_name='property',  
        verbose_name='Relatório Principal'
    )

    class Meta:
        verbose_name = 'Imóvel'
