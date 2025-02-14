from django.contrib import admin
from .models import Event
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class TinyMce(ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE,}
    }

admin.site.register(Event,TinyMce)
