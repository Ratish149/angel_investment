# Generated by Django 5.1.6 on 2025-02-13 09:47

import blog.models
import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('picture', models.FileField(blank=True, null=True, upload_to='')),
                ('about', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('category_image', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=300, null=True, unique=True)),
                ('title', models.CharField(max_length=500)),
                ('blog_duration_to_read', models.CharField(blank=True, max_length=100)),
                ('thumbnail_image', models.FileField(blank=True, null=True, upload_to='')),
                ('thumbnail_image_alt_description', models.CharField(blank=True, max_length=300, null=True)),
                ('blog_content', tinymce.models.HTMLField(blank=True)),
                ('meta_title', models.CharField(max_length=200)),
                ('meta_description', models.CharField(blank=True, max_length=500)),
                ('meta_keywords', models.CharField(blank=True, max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
            bases=(blog.models.SlugMixin, models.Model),
        ),
    ]
