from django.contrib import admin
from .models import Author,Category,Post,Tag
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models

admin.site.register(Author, ModelAdmin)
admin.site.register(Category, ModelAdmin)
admin.site.register(Tag, ModelAdmin)


class TinyMce(ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category', 'blog_duration_to_read')
    list_filter = ('author', 'category', 'created_at', 'tags')
    search_fields = ('title', 'content', 'author__name', 'tags__tag_name')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE,},
    }
admin.site.register(Post,TinyMce)
