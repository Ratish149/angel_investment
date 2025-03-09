from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Contact, Newsletter
# Register your models here.

admin.site.register(Contact, ModelAdmin)
admin.site.register(Newsletter, ModelAdmin)