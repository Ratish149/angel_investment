from django.db import models

# Create your models here.


class CohortMember(models.Model):
    cohort = models.ForeignKey('Cohort', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class Cohort(models.Model):
    PARTICIPATING_STATUS = {
        ('startup', 'startup'),
        ('investor', 'investor')
    }
    company_name = models.CharField(max_length=100)
    company_Logo = models.FileField(
        upload_to='company_logo/', null=True, blank=True)
    company_address = models.CharField(max_length=100, null=True, blank=True)
    company_email = models.EmailField(null=True, blank=True)
    company_phone = models.CharField(max_length=15, null=True, blank=True)
    company_description = models.TextField()
    participating_status = models.CharField(
        max_length=20, choices=PARTICIPATING_STATUS, null=True, blank=True)

    def __str__(self):
        return self.company_name
