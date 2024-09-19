from django.db import models
from .base_report_model import BaseReport

class DrugReport(BaseReport):
    allSubstances = models.TextField(blank=True, default='')  # Armazenar como string
    materialReceivedObservations = models.TextField(blank=True, default='')
    listOfEnvolvedPeople = models.TextField(blank=True, default='')
    listItensLabels = models.TextField(blank=True, default='')
    listOfPackagings = models.TextField(blank=True, default='')
    listOfMorphology = models.TextField(blank=True, default='')
    listOfGrossMass = models.TextField(blank=True, default='')  # Armazenar diretamente como string
    listOfLiquidMass = models.TextField(blank=True, default='')  # Armazenar diretamente como string
    listOfReturned = models.TextField(blank=True, default='')  # Armazenar diretamente como string
    listOfCounterProof = models.TextField(blank=True, default='')  # Armazenar diretamente como string
    listOfEntranceSeal = models.TextField(blank=True, default='')
    listOfExitseal = models.TextField(blank=True, default='')
    listOfpackagingAndMorphology = models.TextField(blank=True, default='')
    listOfResultOfExams = models.TextField(blank=True, default='')

    def save(self, *args, **kwargs):
        # Nenhuma conversão necessária, apenas chamar o método pai
        super().save(*args, **kwargs)

    def get_list(self, field):
        # Recuperar os dados diretamente como string
        return getattr(self, field, '')

    class Meta:
        verbose_name = 'Laudo de Drogas'
        verbose_name_plural = 'Laudos de Drogas'
