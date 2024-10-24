from django.db import models
import os
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

    # Sobrescreve o método save para deletar a imagem antiga
    def save(self, *args, **kwargs):
        try:
            # Verifica se há uma instância antiga com a mesma PK
            old_instance = PropertyReportModel.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                old_image_path = old_instance.image.path
                # Se a imagem antiga existir, exclua
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
        except PropertyReportModel.DoesNotExist:
            # Se o objeto é novo, não há imagem antiga para deletar
            pass

        # Salva a nova instância
        super(PropertyReportModel, self).save(*args, **kwargs)

