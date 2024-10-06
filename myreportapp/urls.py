from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import index, about, contact, login, register, CustomLoginView, reports, drugs_report, userReports, editProfile, theft, editReport, deleteReport


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
    path('user_reports', userReports, name='user_reports'),
    path('edit_profile', editProfile, name='edit_profile'),
    path('furto/', theft, name='furto'),
    path('edit_report/<int:report_id>/', editReport, name='edit_report'),
    path('delete_report/<int:report_id>/', deleteReport, name='delete_report'),
]
