from django.contrib import admin
from .models import CustomUser, Company, CompanyTag, CompanyTeam, Users
from unfold.admin import ModelAdmin
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

class UsersAdmin(ModelAdmin):
    list_display = ('full_name','organization_name','email','contact_number','role','is_activated')
    list_filter = ('role',)
    search_fields = ('full_name','organization_name','email','contact_number')

admin.site.register(Users, UsersAdmin)

