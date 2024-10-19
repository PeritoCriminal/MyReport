from django.db import models
from django.conf import settings
from django.utils import timezone

class HeaderReportModel(models.Model):
    """ A classe HeaderReportModel tem atributos e métdodos comuns dos relatórios em geral """

    report_date = models.DateField('Data do Registro', auto_now_add=True) 
    designation_date = models.DateField('Data de Designação', default=timezone.now) 
    occurrence_date = models.DateField('Data da Ocorrência', default=timezone.now) 
    occurrence_time = models.TimeField('Hora do Atendimento', null=True, default='00:00:00')
    activation_date = models.DateField('Data do Acionamento', default=timezone.now) 
    activation_time = models.TimeField('Hora do Acionamento', null=True, default='00:00:00')
    service_date = models.DateField('Data do Atendimento', default=timezone.now) 
    service_time = models.TimeField('Hora do Atendimento', null=True, default='00:00:00')

    report_number = models.CharField('Número do Laudo', max_length=100, default='', null=True)
    city = models.CharField('Cidade', max_length=100, default='Limeira', null=True)
    protocol_number = models.CharField('Número do Protocolo', max_length=200, default='', null=True)
    police_report_number = models.CharField('Número do Boletim de Ocorrência', max_length=200, default='', null=True)

    examination_objective = models.CharField('Objetivo do Exame', max_length=300, default='')
    incident_nature = models.CharField('Natureza da Ocorrência', max_length=300, default='', null=True)
    police_station = models.CharField('Distrito Policial', max_length=200, default='', null=True)
    requesting_authority = models.CharField('Autoridade Requisitante', max_length=200, default='', null=True)

    institute_director = models.CharField('Diretor do Instituto', max_length=200, default='')
    institute_unit = models.CharField('Núcleo do Instituto', max_length=200, default='')
    forensic_team_base = models.CharField('Base da Equipe de Perícias', max_length=200, default='')
    expert_display_name = models.CharField('Perito', max_length=200, default='')

    reporting_expert = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        verbose_name='Perito Relator'
    )
    
    photographer = models.CharField('Fotógrafo', max_length=200, blank=True, null=True, default='')

    considerations = models.TextField('Considerações', blank=True, default='')
    conclusion = models.TextField('Conclusão', blank=True, default='')

    def save(self, *args, **kwargs):
        """Sobrescreve o método save para copiar o full_name do usuário"""
        if self.reporting_expert:
            print(f'Nome completo do usuário: {self.reporting_expert.full_name}')
            self.expert_display_name = self.reporting_expert.full_name
        else:
            print(f'Não tem o usuário.')
        super().save(*args, **kwargs)

    @classmethod
    def notify_default_dates(cls):
        """Retorna uma mensagem para o usuário caso haja datas com valor default"""
        return """
        Algumas datas estão com o valor padrão de 01-01-1900. Reveja as antes de finalizar o relatório.
        """
    
    
    def dateToForm(self, date_field = '1900-01-01'):
        """Converte qualquer uma das datas cadastradas no formato 'yyyy-mm-dd'"""
        if date_field:
            try:
                return date_field.strftime('%Y-%m-%d')
            except (ValueError, AttributeError):
                return '1900-01-01'
        return '1900-01-01'
    
    
    def hourToForm(self, time_field = '00:00'):
        """Converte qualquer uma das horas cadastradas no formato 'HH:MM'"""
        if time_field:
            try:
                return time_field.strftime('%H:%M')
            except (ValueError, AttributeError):
                return '00:00'
        return '00:00'


    def __str__(self):
        return f'Relatório {self.report_number} - Perito: {self.expert_display_name}'

    class Meta:
        verbose_name = 'Relatório Pericial'
        verbose_name_plural = 'Relatórios Periciais'
