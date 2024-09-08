from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from ..forms.user_login_form import UserLoginForm

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('reports')
    