# Generated by Django 5.1.6 on 2025-03-16 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_users_organization_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='organization_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
