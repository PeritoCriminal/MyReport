"""

Copyright (c) 2024 Marcos de Oliveira Capristo
Todos os direitos reservados.

MYREPORT é um projeto independente.
Oferece um ambiente para edição de laudos periciais,
voltado especialmente para Peritos Criminais Oficiais do Estado de São Paulo.
Idealizado e inicialmente desenvolvido pelo Perito Criminal Marcos de Oliveira Capristo.
Contato: marcos.moc@policiacientifica.sp.gov.br | (19) 9 8231-2774


"""


from .index import index
from .contact import contact
from .about import about
from .login import login
from .user_register import register
from .user_login_views import CustomLoginView
from .reports import reports
from .drugs_report import drugs_report
from .edit_profile import editProfile
from .user_reports import userReports
from .theft import theft_report_view
from .edit_report import editReport
from .delete_reports import deleteReport
from .header_report_view import HeaderReportView
from .viewbase import adicionar_rodape
