from django.contrib import admin
from .models import CustomUser, Company, CompanyTag, CompanyTeam
from unfold.admin import ModelAdmin
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class CustomUserAdmin(ModelAdmin):
    list_display = ('full_name','email', 'role', 'is_activated','is_staff')
    list_filter = ('role', 'is_activated')
    search_fields = ('full_name','email','first_name')


class CompanyAdmin(ModelAdmin):
    list_display = ('company_name', 'stage', 'contact_city', 'contact_country', 'contact_phone_number', 'contact_email', 'website', 'amount_raising', 'affiliation')
    list_filter = ('stage', 'contact_city', 'contact_country', 'amount_raising', 'affiliation')
    search_fields = ('company_name', 'contact_city', 'contact_country', 'contact_email', 'website', 'amount_raising', 'affiliation')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE,},
    }

class CompanyTagAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CompanyTeamAdmin(ModelAdmin):
    list_display = ('name', 'position', 'linkedin')
    search_fields = ('name', 'position', 'linkedin')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyTag, CompanyTagAdmin)
admin.site.register(CompanyTeam, CompanyTeamAdmin)
