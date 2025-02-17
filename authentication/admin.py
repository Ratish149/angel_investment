from django.contrib import admin
from .models import CustomUser, Company, CompanyTag, CompanyTeam
from unfold.admin import ModelAdmin
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class CustomUserAdmin(ModelAdmin):
    list_display = ('full_name','email', 'get_company_name','role', 'is_activated','is_staff')
    list_filter = ('role', 'is_activated')
    search_fields = ('full_name','email','first_name')

    def get_company_name(self, obj):
        return ", ".join([company.company_name for company in obj.company_set.all()])
    get_company_name.short_description = 'Company Name'

class CompanyAdmin(ModelAdmin):
    list_display = ('company_name', 'stage', 'contact_city', 'contact_country', 'contact_phone_number', 'contact_email', 'website', 'amount_raising', 'affiliation')
    list_filter = ('stage', 'contact_city', 'contact_country', 'amount_raising', 'affiliation')
    search_fields = ('company_name', 'contact_city', 'contact_country', 'contact_email', 'website', 'amount_raising', 'affiliation')


class CompanyTagAdmin(ModelAdmin):
    list_display = ('name','get_company_name')
    search_fields = ('name',)
    def get_company_name(self, obj):
        return ", ".join([company.company_name for company in obj.company_set.all()])
    get_company_name.short_description = 'Company Name'

class CompanyTeamAdmin(ModelAdmin):
    list_display = ('name', 'position', 'linkedin', 'get_company_name')
    search_fields = ('name', 'position', 'linkedin')

    def get_company_name(self, obj):
        return ", ".join([company.company_name for company in obj.company_set.all()])
    get_company_name.short_description = 'Company Name'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyTag, CompanyTagAdmin)
admin.site.register(CompanyTeam, CompanyTeamAdmin)
