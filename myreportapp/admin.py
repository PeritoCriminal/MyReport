from django.contrib import admin
from .models import UserRegistrationModel

@admin.register(UserRegistrationModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'city', 'unit', 'team')
    search_fields = ('username', 'full_name', 'email', 'city')
    list_filter = ('city', 'unit', 'team')
