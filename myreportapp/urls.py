from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import index, about, contact, login, register, CustomLoginView, reports, drugs_report


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login', login, name='login'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('reports/', reports, name='reports'),
    path('drugs/', drugs_report, name='drugs_report'),
]
