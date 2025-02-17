from django.db import models
from blog.models import SlugMixin
# Create your models here.

class Academy(SlugMixin,models.Model):
    title = models.CharField(max_length=220)
    slug=models.SlugField(max_length=220, unique=True, null=True, blank=True)
    logo = models.FileField(upload_to='chapter_logos/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Article(SlugMixin,models.Model):
    academy=models.ForeignKey(Academy, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=220)
    slug=models.SlugField(max_length=220, unique=True, null=True, blank=True)
    description=models.TextField()
    content=models.TextField(null=True, blank=True)
    file=models.FileField(upload_to='academy_files/', null=True, blank=True)
    video_link=models.URLField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

