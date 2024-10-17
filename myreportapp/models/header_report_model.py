from django.db import models
from django.conf import settings

class HeaderReportModel(models.Model):
    """ A classe HeaderReportModel tem atributos e métdodos comuns dos relatórios em geral """

    # Atributos de data e hora com valor padrão 01-01-1900 para datas display
    report_date = models.DateField('Data do Registro', default='1900-01-01')
    designation_date = models.DateField('Data de Designação', default='1900-01-01')
    occurrence_date = models.DateField('Data da Ocorrência', default='1900-01-01')
    occurrence_time = models.TimeField('Hora do Atendimento', null=True, default='00:00:00')
    activation_date = models.DateField('Data do Acionamento', default='1900-01-01')
    activation_time = models.TimeField('Hora do Acionamento', null=True, default='00:00:00')
    service_date = models.DateField('Data do Atendimento', default='1900-01-01')
    service_time = models.TimeField('Hora do Atendimento', null=True, default='00:00:00')

    # Atributos de identificação
    report_number = models.CharField('Número do Laudo', max_length=100, default='', null=True)
    city = models.CharField('Cidade', max_length=100, default='Limeira', null=True)
    protocol_number = models.CharField('Número do Protocolo', max_length=200, default='', null=True)
    police_report_number = models.CharField('Número do Boletim de Ocorrência', max_length=200, default='', null=True)

    # Atributos relacionados ao exame
    examination_objective = models.CharField('Objetivo do Exame', max_length=300, default='')
    incident_nature = models.CharField('Natureza da Ocorrência', max_length=300, default='', null=True)
    police_station = models.CharField('Distrito Policial', max_length=200, default='', null=True)
    requesting_authority = models.CharField('Autoridade Requisitante', max_length=200, default='', null=True)

    # Atributos relacionados ao instituto e equipe
    institute_director = models.CharField('Diretor do Instituto', max_length=200, default='')
    institute_unit = models.CharField('Núcleo do Instituto', max_length=200, default='')
    forensic_team_base = models.CharField('Base da Equipe de Perícias', max_length=200, default='')

    # Atributos relacionados ao perito e fotógrafo
    reporting_expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='Perito Relator'
    )
    expert_display_name = models.CharField(
        'Nome do Perito Exibido no Relatório', 
        max_length=200
    )
    photographer = models.CharField('Fotógrafo', max_length=200, blank=True, null=True, default='')

    # Atributos de considerações e conclusão
    considerations = models.TextField('Considerações', blank=True, default='')
    conclusion = models.TextField('Conclusão', blank=True, default='')

    def save(self, *args, **kwargs):
        """Sobrescreve o método save para copiar o display_name do usuário"""
        if self.reporting_expert:
            self.expert_display_name = 'self.reporting_expert.display_name'  # Copia o display_name do usuário
        super().save(*args, **kwargs)

    @classmethod
    def notify_default_dates(cls):
        """Retorna uma mensagem para o usuário caso haja datas com valor default"""
        return """
        Algumas datas estão com o valor padrão de 01-01-1900. Reveja as antes de finalizar o relatório.
        """

    def __str__(self):
        return f'Relatório {self.report_number} - Perito: {self.expert_display_name}'

    class Meta:
        verbose_name = 'Relatório Pericial'
        verbose_name_plural = 'Relatórios Periciais'
