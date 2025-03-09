from django.db import models

# Create your models here.

class Contact(models.Model):
    CHOICES={
        ('Investor', 'Investor'),
        ('Mentor', 'Mentor'),
        ('Startup', 'Startup')
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number=models.CharField(max_length=20)
    message = models.TextField()
    who_are_you = models.CharField(max_length=20, choices=CHOICES,blank=True, null=True)

    def __str__(self):
        return self.first_name
    
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email