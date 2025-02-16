from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Academy, Chapter
# Register your models here.

@admin.register(Chapter)
class ChapterAdmin(ModelAdmin):
    list_display = ('title', 'description')  # Display title and description in the list
    search_fields = ('title',)  # Add search filter for title

@admin.register(Academy)
class AcademyAdmin(ModelAdmin):
    list_display = ('title', 'chapter', 'created_at')  # Display title, chapter, and created_at in the list
    list_filter = ('chapter', 'created_at')  # Add filters for chapter and created_at
    search_fields = ('title', 'description')  # Add search filter for title and description
