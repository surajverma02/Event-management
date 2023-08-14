from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    eventname = models.CharField(max_length=100)
    event_date = models.CharField(max_length=200)
    price_started = models.IntegerField(default=0)
    location = models.TextField(max_length=500)
    image = models.ImageField(upload_to="events/")
    is_like = models.BooleanField(default=False, null=True, blank=True)
    
    def __str__(self):
        return self.eventname

