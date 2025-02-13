from django.contrib import admin
from .models import Author,Category,Post,Tag
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django.db import models

admin.site.register(Author, ModelAdmin)
admin.site.register(Category, ModelAdmin)
admin.site.register(Tag, ModelAdmin)


# class PostAdmin(ModelAdmin):
#    formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()},
#     }
   
# admin.site.register(Post,PostAdmin)
admin.site.register(Post,ModelAdmin)
