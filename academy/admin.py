from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Academy, Article
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

@admin.register(Academy)
class AcademyAdmin(ModelAdmin):
    list_display = ('title', 'description')  # Display title and description in the list
    search_fields = ('title',)  # Add search filter for title

@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ('title', 'academy', 'created_at')  # Display title, chapter, and created_at in the list
    list_filter = ('academy', 'created_at')  # Add filters for chapter and created_at
    search_fields = ('title', 'description')  # Add search filter for title and description
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE, },
    }
