from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Academy, Article, Documents
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


@admin.register(Academy)
class AcademyAdmin(ModelAdmin):
    # Display title and description in the list
    list_display = ('title', 'description')
    search_fields = ('title',)  # Add search filter for title


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    # Display title, chapter, and created_at in the list
    list_display = ('title', 'academy', 'created_at')
    # Add filters for chapter and created_at
    list_filter = ('academy', 'created_at')
    # Add search filter for title and description
    search_fields = ('title', 'description')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE, },
    }


@admin.register(Documents)
class DocumentsAdmin(ModelAdmin):
    # Display file and created_at in the list
    list_display = ('order', 'file', 'created_at')
    list_filter = ('created_at',)  # Add filter for created_at
    search_fields = ('file',)  # Add search filter for file
