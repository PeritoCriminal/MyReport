from django.db import models
from ..models import HeaderReportModel

class ScenePreservationReportModel(models.Model):
    description = models.TextField(blank=True, verbose_name='Preservação - Descrição', default='')
    reportForeignKey = models.ForeignKey(
        HeaderReportModel, 
        on_delete=models.CASCADE,  
        related_name='scene_preservations',  
        verbose_name='Relatório Principal'
    )

    class Meta:
        verbose_name = 'Preservação de Local'
