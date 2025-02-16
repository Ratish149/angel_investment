from django.db import models

# Create your models here.

class Chapter(models.Model):
    title = models.CharField(max_length=220)
    logo = models.FileField(upload_to='chapter_logos/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Academy(models.Model):
    chapter=models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=220)
    description=models.TextField()
    content=models.TextField(null=True, blank=True)
    file=models.FileField(upload_to='academy_files/', null=True, blank=True)
    video_link=models.URLField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

