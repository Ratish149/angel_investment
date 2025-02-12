# Generated by Django 5.1.6 on 2025-02-11 09:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_companyteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='about_startup',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='checkmark1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='checkmark2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='checkmark3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='company_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='startup_image',
            field=models.FileField(blank=True, null=True, upload_to='startup_images/'),
        ),
        migrations.AddField(
            model_name='company',
            name='startup_video',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='tile_image',
            field=models.FileField(blank=True, null=True, upload_to='company_tile_images/'),
        ),
        migrations.AddField(
            model_name='companyteam',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='authentication.company'),
            preserve_default=False,
        ),
    ]
