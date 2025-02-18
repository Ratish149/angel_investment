from django.contrib import admin
from .models import Event
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

# ... existing imports ...

class TinyMce(ModelAdmin):
    list_display = ('title', 'event_date', 'event_location', 'created_at', 'updated_at')
    search_fields = ('title', 'event_location')
    list_filter = ('event_date', 'event_location')
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }

admin.site.register(Event,TinyMce)
