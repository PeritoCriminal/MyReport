from django.contrib import admin
from .models import UserRegistrationModel, DrugReport, TheftReportModel

@admin.register(UserRegistrationModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'city', 'unit', 'team')
    search_fields = ('username', 'full_name', 'email', 'city')
    list_filter = ('city', 'unit', 'team')

@admin.register(DrugReport)
class DrugReportAdmin(admin.ModelAdmin):
    list_display = ('protocol_number', 'police_station', 'allSubstances')
    search_fields = ('protocol_number', 'police_station')
    list_filter = ('police_station',)

@admin.register(TheftReportModel)
class TheftTheftReportModelAdmin(admin.ModelAdmin):
    list_display = ('protocol_number', 'police_station')
    search_fields = ('protocol_number', 'police_station')
    list_filter = ('police_station',)
