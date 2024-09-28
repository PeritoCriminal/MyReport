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

VIEW LOGIN, A MELHORAR


"""



from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from ..forms.user_login_form import UserLoginForm

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('reports')
    