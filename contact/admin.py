from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Contact, Newsletter, BookSpace
# Register your models here.


class BookSpaceAdmin(ModelAdmin):
    list_display = ('name', 'email', 'phone_number',
                    'date_and_time',)
    list_filter = ('date_and_time',)
    search_fields = ('name', 'email', 'phone_number')
    ordering = ('-created_at',)


admin.site.register(Contact, ModelAdmin)
admin.site.register(Newsletter, ModelAdmin)
admin.site.register(BookSpace, BookSpaceAdmin)
