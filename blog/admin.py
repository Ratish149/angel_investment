from django.contrib import admin
from .models import Author,Category,Post,Tag,Faq
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models

class AuthorAdmin(ModelAdmin):
    list_display = ('name', 'role', 'phone', 'created_at')  # Specify fields to display
    search_fields = ('name', 'role', 'phone')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, ModelAdmin)

class TagAdmin(ModelAdmin):
    list_display = ('tag_name',)
    search_fields = ('post__title',)
    list_filter = ('post__title',)

admin.site.register(Tag, TagAdmin)

class TinyMce(ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category', 'blog_duration_to_read')
    list_filter = ('author', 'category', 'created_at', 'tags')
    search_fields = ('title', 'content', 'author__name', 'tags__tag_name')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE,},
    }

# Add list_display and list_filter for Faq
class FaqAdmin(ModelAdmin):
    list_display = ('question', 'category', 'created_at')
    list_filter = ('category',)
    
admin.site.register(Post,TinyMce)
admin.site.register(Faq, FaqAdmin)
