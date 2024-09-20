from django.db import models
from .base_report_model import BaseReport

class DrugReport(BaseReport):
    allSubstances = models.TextField(blank=True, verbose_name='Substâncias examinadas', default='')
    materialReceivedObservations = models.TextField(blank=True, verbose_name='Observações sobre o material recebido', default='')

    # Imagem do material e sua respectiva legenda
    materialImage = models.TextField(blank=True, verbose_name='imagem do Material Recebido', default='')
    materialImageCaption = models.TextField(blank=True, verbose_name='Legenda da fotografia do material', default='')

    listOfEnvolvedPeople = models.TextField(blank=True, verbose_name='Pessoas envolvidas', default='')
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
    listOfReturneds = models.TextField(blank=True, verbose_name='Material retornado e contraperícia', default='')

    # Lista de imagens e legendas
    examImages = models.TextField(blank=True, verbose_name='imagem do item examinado', default='')
    examImageCaptions = models.TextField(blank=True, verbose_name='Legendas da imagem do item examinado', default='')

    # Imagem dos itens retornados e legenda
    returnedItemsImage = models.TextField(blank=True, verbose_name='imagem do Material Retornado', default='')
    returnedItemsCaption = models.TextField(blank=True, verbose_name='Legenda do Material retornado', default='')

    # Imagem da contraperícia e legenda
    counterProofImage = models.TextField(blank=True, verbose_name='imagem do material separado para contraperícia', default='')
    counterProofCaption = models.TextField(blank=True, verbose_name='Legenda da contraperícia', default='')

    def save(self, *args, **kwargs):
        # Nenhuma conversão necessária, apenas chamar o método pai
        super().save(*args, **kwargs)

    def get_list(self, field):
        # Recuperar os dados diretamente como string
        return getattr(self, field, '')

    class Meta:
        verbose_name = 'Laudo de Drogas'
        verbose_name_plural = 'Laudos de Drogas'
