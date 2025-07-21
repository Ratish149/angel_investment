from django.contrib import admin
from .models import Event, EventAttendee
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

# ... existing imports ...


class TinyMce(ModelAdmin):
    list_display = ('title', 'event_date', 'event_location',
                    'created_at', 'updated_at')
    search_fields = ('title', 'event_location')
    list_filter = ('event_date', 'event_location')

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE}
    }


class EventAttendeeAdmin(ModelAdmin):
    list_display = ('event', 'email', 'created_at')
    search_fields = ('event', 'email')
    list_filter = ('event', 'created_at')


admin.site.register(Event, TinyMce)
admin.site.register(EventAttendee, EventAttendeeAdmin)
