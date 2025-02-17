# Generated by Django 5.1.6 on 2025-02-16 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('logo', models.FileField(blank=True, null=True, upload_to='chapter_logos/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField()),
                ('content', models.TextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='academy_files/')),
                ('video_link', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='academy.chapter')),
            ],
        ),
    ]
