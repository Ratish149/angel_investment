# Generated by Django 5.1.6 on 2025-02-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0004_academy_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=220, null=True, unique=True),
        ),
    ]
