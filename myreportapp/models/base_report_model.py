"""

Copyright (c) 2024 Marcos de Oliveira Capristo
Todos os direitos reservados.

MYREPORT é um projeto independente.
Oferece um ambiente para edição de laudos periciais,
voltado especialmente para Peritos Criminais Oficiais do Estado de São Paulo.
Idealizado e inicialmente desenvolvido pelo Perito Criminal Marcos de Oliveira Capristo.
Contato: marcos.moc@policiacientifica.sp.gov.br | (19) 9 8231-2774


"""

"""

MODEL BASE PARA OS LAUDOS

"""


from django.db import models
from datetime import datetime
import locale

class BaseReport(models.Model):
    date_register = models.DateField('Data do Registro', auto_now_add=True)
    report_number = models.CharField('Número do Laudo', max_length=20, default='indefinido')
    city = models.CharField('Cidade', max_length=50, default='Limeira')
    protocol_number = models.CharField('Número do Protocolo', max_length=20, default='indefinido')
    occurring_number = models.CharField('Número do Boletim', max_length=20, default='indefinido')
    designated_date = models.CharField('Data de Designação', max_length=20, blank=True, null=True)
    exam_objective = models.CharField('Objetivo do Exame', max_length=300, default='indefinido')
    occurrence_nature = models.CharField('Natureza da Ocorrência', max_length=300, default='indefinido')
    police_station = models.CharField('Distrito Policial', max_length=200, default='indefinido')
    requesting_authority = models.CharField('Autoridade Requisitante', max_length=200, default='indefinido')
    activation_date = models.CharField('Data do Acionamento', max_length=20, blank=True, null=True)
    activation_time = models.TimeField('Hora do Acionamento', auto_now=False, blank=True, null=True)
    service_date = models.CharField('Data do Atendimento', max_length=20)
    service_time = models.TimeField('Hora do Atendimento', auto_now=False, blank=True, null=True)
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

    def setDateDefault(self):
        pass
    
    def generate_objective(self):
        objective_text = f"Objetivo do exame, de acordo com a requisição: {self.exam_objective}."
        return objective_text

    def generate_occurrence_nature(self):
        occurrence_nature_text = f"Natureza da ocorrência, de acordo com a requisição: {self.occurrence_nature}."
        return occurrence_nature_text
    



    def format_date(self, date_str):
        # Define a localidade para português do Brasil
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  
        
        # Lista de possíveis formatos de data
        formatos = ['%d-%m-%Y', '%Y-%m-%d']
        
        for formato in formatos:
            try:
                # Tenta converter a string para um objeto datetime
                date_object = datetime.strptime(date_str, formato)
                # Formata a data no formato desejado
                formatted_date = date_object.strftime('%d de %B de %Y')
                return formatted_date
            except ValueError:
                # Se der erro, passa para o próximo formato
                continue
        
        # Se nenhum formato corresponder, lança um erro
        raise ValueError("Formato de data não suportado: {}".format(date_str))
    




    def generate_preamble(self):
        formatted_date = self.format_date(self.designated_date)  # Formata a data
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
            expertIs = 'designado(a) o(a) perito(a) criminal'

        if self.requesting_authority.startswith('Dra.'):
            authorityIs = 'a Delegada de Polícia'
        elif self.requesting_authority.startswith('Dr.'):
            authorityIs = 'o Delegado de Polícia'
        else:
            authorityIs = 'o(a) Delegado(a) de Polícia'
        
        preamble = (
            f"Em {formatted_date}, na cidade de {self.city} "
            f"e no Instituto de Criminalística da Superintendência da Polícia Técnico-Científica, " 
            f"da Secretaria de Segurança Pública do Estado de São Paulo, em conformidade com o disposto no art. "
            f"178 do Decreto-Lei 3689, de 3 de outubro de 1941, e no Decreto-Lei 42847, "
            f"de 9 de fevereiro de 1998, {directorIs} {self.director}, "
            f"foi {expertIs} {self.reporting_expert} para proceder ao exame pericial especificado em requisição "
            f"assinada pela Autoridade Policial, {authorityIs} {self.requesting_authority}."
        )
        return preamble
