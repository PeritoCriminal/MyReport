from django.db import models
from .base_report_model import BaseReport

class DrugReport(BaseReport):
    allSubstances = models.TextField(blank=True, verbose_name='Substâncias examinadas', default='')
    materialReceivedObservations = models.TextField(blank=True, verbose_name='Observações sobre o material recebido', default='')

    # Imagem do material e sua respectiva legenda
    materialImage = models.ImageField(upload_to='material_images/', blank=True, verbose_name='Fotografia do material')
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
    examImages = models.ImageField(upload_to='exam_images/', blank=True, verbose_name='Imagens dos exames')
    examImageCaptions = models.TextField(blank=True, verbose_name='Legendas das imagens dos exames', default='')

    # Imagem dos itens retornados e legenda
    returnedItemsImage = models.ImageField(upload_to='returned_items_images/', blank=True, verbose_name='Imagem dos itens retornados')
    returnedItemsCaption = models.TextField(blank=True, verbose_name='Legenda dos itens retornados', default='')

    # Imagem da contraperícia e legenda
    counterProofImage = models.ImageField(upload_to='counterproof_images/', blank=True, verbose_name='Imagem da contraperícia')
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
