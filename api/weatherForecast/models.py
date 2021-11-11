from django.db import models

class Weather(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=False)
    country_code = models.CharField(max_length=2, blank=False)
    temperature = models.FloatField(blank=False)
