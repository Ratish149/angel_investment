from django.db import models

# Create your models here.

class Event(models.Model):
    title=models.CharField(max_length=100)
    event_details=models.TextField()
    event_date=models.DateTimeField()
    event_location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class EventAttendee(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    email=models.EmailField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    