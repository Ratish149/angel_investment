from django.db import models

# Create your models here.


class Contact(models.Model):
    CHOICES = {
        ('Investor', 'Investor'),
        ('Mentor', 'Mentor'),
        ('Startup', 'Startup')
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    who_are_you = models.CharField(
        max_length=20, choices=CHOICES, blank=True, null=True)
    privacy_agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class BookSpace(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_and_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
