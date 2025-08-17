from django.contrib import admin
from .models import Cohort, CohortMember
from unfold.admin import ModelAdmin, TabularInline
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.


class CohortMemberAdmin(TabularInline):
    model = CohortMember
    tab = True


class CohortAdmin(ModelAdmin):
    model = Cohort
    inlines = [CohortMemberAdmin]
    tab = True
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE, },
    }


admin.site.register(Cohort, CohortAdmin)
admin.site.register(CohortMember)
