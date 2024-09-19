from django.db import models
from .base_report_model import BaseReport

class DrugReport(BaseReport):
    allSubstances = models.TextField(blank=True, default='')
    materialReceivedObservations = models.TextField(blank=True, verbose_name='Todas as substâncias', default='')
    listOfEnvolvedPeople = models.TextField(blank=True, verbose_name='Pessoas envolvidas', default='')
    # listItensLabels = models.TextField(blank=True, verbose_name='Itens', default='') não tem função
    listOfPackagings = models.TextField(blank=True, verbose_name='Embalagens', default='')
    listOfMorphology = models.TextField(blank=True, verbose_name='Morfologia', default='')
    listOfGrossMass = models.TextField(blank=True, verbose_name='Massa bruta', default='') 
    listOfLiquidMass = models.TextField(blank=True, verbose_name='Massa líquida', default='')  
    listOfReturned = models.TextField(blank=True, verbose_name='Material retornado', default='')  
    listOfCounterProof = models.TextField(blank=True, verbose_name='Contraperícia', default='') 
    listOfEntranceSeal = models.TextField(blank=True, verbose_name='Lacre de entrada', default='')
    listOfExitseal = models.TextField(blank=True, verbose_name='Lacre de saída', default='')
    listOfpackagingAndMorphology = models.TextField(blank=True, verbose_name='Descrição do item', default='')
    listOfResultOfExams = models.TextField(blank=True, verbose_name='Resultado do exame', default='')

    def save(self, *args, **kwargs):
        # Nenhuma conversão necessária, apenas chamar o método pai
        super().save(*args, **kwargs)

    def get_list(self, field):
        # Recuperar os dados diretamente como string
        return getattr(self, field, '')

    class Meta:
        verbose_name = 'Laudo de Drogas'
        verbose_name_plural = 'Laudos de Drogas'
