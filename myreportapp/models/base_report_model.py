from django.db import models
from datetime import datetime


class BaseReport(models.Model):
    date_register = models.DateField('Data do Registro', auto_now_add=True)
    report_number = models.CharField('Número do Laudo', max_length=20, default='indefinido')
    city = models.CharField('Número do Laudo', max_length=50, default='Limeira')
    protocol_number = models.CharField('Número do Protocolo', max_length=20, default='indefinido')
    occurring_number = models.CharField('Número do Boletim', max_length=20, default='indefinido')
    designated_date = models.CharField('Data de Designação',  max_length=20, default='data indefinida!')
    exam_objective = models.CharField('Objetivo do Exame', max_length=300, default='indefinido')
    occurrence_nature = models.CharField('Natureza da Ocorrência', max_length=300, default='indefinido')
    police_station = models.CharField('Distrito Policial', max_length=200, default='indefinido')
    requesting_authority = models.CharField('Autoridade Requisitante', max_length=200, default='indefinido')
    activation_date = models.CharField('Data do Acionamento',  max_length=20, default='data indefinida!')
    activation_time = models.TimeField('Hora do Acionamento', auto_now=False, blank=True, null=True)
    service_date = models.CharField('Data do Atendimento',  max_length=20, default='data indefinida!')
    service_time = models.TimeField('Hora do Atendimento', auto_now=False)
    director = models.CharField('Diretor', max_length=200, default='indefinido')
    nucleus = models.CharField('Núcleo', max_length=200, default='indefinido')
    team = models.CharField('Equipe de Perícias', max_length=200, default='indefinido')
    reporting_expert = models.CharField('Perito Relator', max_length=100, default='indefinido')
    assistant_expert = models.CharField('Perito Assistente', max_length=100, blank=True, null=True, default='indefinido')
    photographer = models.CharField('Fotógrafo', max_length=100, blank=True, null=True, default='indefinido')
    draftsman = models.CharField('Desenhista', max_length=100, blank=True, null=True, default='indefinido')
    considerations = models.TextField(blank=True, verbose_name='Considerações', default='')
    conclusion = models.TextField(blank=True, verbose_name='Conclusão', default='')

    class Meta:
        abstract = True

    def setDateDefault():
        pass
    
    def generate_objective(self):
        objective_text = f"Objetivo do exame, de acordo com a requisição: {self.exam_objective}."
        return objective_text

    def generate_occurrence_nature(self):
        occurrence_nature_text = f"Natureza da ocorrência, de acordo com a requisição: {self.occurrence_nature}."
        return occurrence_nature_text
    
    def generate_preamble(self):
        if self.director.startswith('Dra'):
            directorIs = 'pela Diretora deste Instituto de Criminalística, a Perita Criminal'
        elif self.director.startswith('Dr.'):
            directorIs = 'pelo Diretor deste Instituto de Criminalística, o Perito Criminal'
        else:
            directorIs = 'pelo(a) Diretor(a) deste Instituto de Criminalística, o(a) Perito(a) Criminal'

        if self.reporting_expert.startswith('Dra.'):
            expertIs = 'designada a perita criminal'
        elif self.reporting_expert.startswith('Dr.'):
            expertIs = 'designado o perito criminal'
        else:
            expertIs = 'o(a) perito(a) criminal'

        if self.requesting_authority.startswith('Dra.'):
            authorityIs = 'a Delegada de Polícia'
        elif self.requesting_authority.startswith('Dr.'):
            authorityIs = 'o Delegado de Polícia'
        else:
            authorityIs = 'o(a) Delegado(a) de Polícia'
        preamble = (
            f"Em {self.designated_date}, na cidade de {self.city} e no Instituto de Criminalística, "
            f"da Superintendência da Polícia Técnico-Científica, da Secretaria de Segurança Pública do Estado de São Paulo, "
            f"em conformidade com o disposto no art. 178 do Decreto-Lei 3689 de 3-10-1941 e Decreto-Lei 42847 de 9-2-1998, "
            f"{directorIs} {self.director}, foi {expertIs} "
            f"{self.reporting_expert} para proceder ao Exame Pericial especificado em requisição de exame assinada pela Autoridade Policial, "
            f"{authorityIs} {self.requesting_authority}."
        )
        return preamble
    