from django.contrib import admin
from .models import UserRegistrationModel, DrugReport  # Importe o DrugReport

@admin.register(UserRegistrationModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'city', 'unit', 'team')
    search_fields = ('username', 'full_name', 'email', 'city')
    list_filter = ('city', 'unit', 'team')

@admin.register(DrugReport)
class DrugReportAdmin(admin.ModelAdmin):
    # Exibir apenas os campos especificados
    list_display = ('protocol_number', 'police_station', 'allSubstances')
    
    # Habilitar campos de busca
    search_fields = ('protocol_number', 'police_station')
    
    # Filtrar pelo campo police_stat, se necessário
    list_filter = ('police_station',)
