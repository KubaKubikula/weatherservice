from django.db import models

class Weather(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    countryCode = models.CharField(max_length=2, blank=True, default='')
    temperature = models.CharField(max_length=4, blank=True, default='')
