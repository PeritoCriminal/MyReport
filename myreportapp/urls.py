from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import index, about, contact, login, register, CustomLoginView, reports, drugs_report, userReports, editProfile, theft, deleteReport, HeaderReportView, ModulesReportView


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
    path('furto/', theft.theft_report_view, name='furto'),
    path('furto/<int:report_id>/', theft.theft_report_view, name='edit_report'),    
    path('furto/<int:report_id>/', theft.theft_report_view, name='theft_report_view'),
    path('furto/generate-docx/<int:report_id>/', theft.generate_theft_docx, name='generate_theft_docx'),
    path('delete_report/<int:report_id>/', deleteReport, name='delete_report'),

    path('headerreport', HeaderReportView, name='header_report'),
    path('headerreport/<int:report_id>/', HeaderReportView, name='edit_header_report'),
    path('modulesreport/<int:report_id>/', ModulesReportView, name='modules_report'),
]
