from django.contrib import admin
from .models import OurTeam, OurPartner
from unfold.admin import ModelAdmin
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.


class OurTeamAdmin(ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'role', 'email', 'created_at')
    search_fields = ('name', 'role')  # Fields to search in the admin
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class OurPartnerAdmin(ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(OurPartner, OurPartnerAdmin)
