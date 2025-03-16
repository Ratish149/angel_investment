from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Investor', 'Investor'),
        ('Mentor', 'Mentor'),
        ('Startup', 'Startup')
    )
    full_name = models.CharField(max_length=100)
    photo=models.FileField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_activated = models.BooleanField(default=False)
    def __str__(self):
        return self.email
    
class Users(models.Model):
    ORGANIZATION_ROLE_CHOICES = (
        ('Investor', 'Investor'),
        ('Mentor', 'Mentor'),
        ('Startup', 'Startup')
    )
    
    ROLE_CHOICES = (
        ('Founder', 'Founder'),
        ('Employee', 'Employee')
    )
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    contact_number=models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True, blank=True)
    organization_name=models.CharField(max_length=100, null=True, blank=True)
    organization_role = models.CharField(max_length=10, choices=ORGANIZATION_ROLE_CHOICES, null=True, blank=True)
    organization_logo=models.FileField(upload_to='organization_logos/', null=True, blank=True)
    organization_description=models.TextField(null=True, blank=True)
    website_link=models.URLField(max_length=100, null=True, blank=True)
    document=models.FileField(upload_to='documents/', null=True, blank=True)
    is_activated=models.BooleanField(default=False)
    verification_code=models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.organization_name}"

class CompanyTag(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class CompanyTeam(models.Model):
    name=models.CharField(max_length=100)
    profile_picture=models.FileField(upload_to='team_profiles/', null=True, blank=True)
    bio=models.TextField(null=True, blank=True)
    position=models.CharField(max_length=100, null=True, blank=True)
    linkedin=models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    STAGE_CHOICES=(
        ('Idea', 'Idea'),
        ('MVP', 'MVP'),
        ('First Revenue', 'First Revenue'),
        ('Scaling', 'Scaling'),
    )
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    tags=models.ManyToManyField(CompanyTag, blank=True)
    logo=models.FileField(upload_to='company_logos/', null=True, blank=True)
    trade_name=models.CharField(max_length=100, null=True, blank=True)
    tagline=models.CharField(max_length=45, null=True, blank=True)
    stage=models.CharField(max_length=100,choices=STAGE_CHOICES, null=True, blank=True)

    contact_city=models.CharField(max_length=100, null=True, blank=True)
    contact_country=models.CharField(max_length=100, null=True, blank=True)
    contact_phone_number=models.CharField(max_length=100, null=True, blank=True)
    contact_email=models.EmailField(max_length=100, null=True, blank=True)
    website=models.URLField(max_length=100, null=True, blank=True)
    amount_raising=models.CharField(max_length=100, null=True, blank=True)
    affiliation=models.CharField(max_length=100, null=True, blank=True)

    team_members=models.ManyToManyField(CompanyTeam, blank=True)

    tile_image=models.FileField(upload_to='company_tile_images/', null=True, blank=True)
    company_description=models.TextField(null=True, blank=True)
    startup_image=models.FileField(upload_to='startup_images/', null=True, blank=True)
    startup_video=models.TextField(null=True, blank=True)
    checkmark1=models.CharField(max_length=100, null=True, blank=True)
    checkmark2=models.CharField(max_length=100, null=True, blank=True)
    checkmark3=models.CharField(max_length=100, null=True, blank=True)
    about_startup=models.TextField(null=True, blank=True)
    featured=models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


