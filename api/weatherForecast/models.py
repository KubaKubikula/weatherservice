from django.db import models

class Weather(models.Model):
    created = models.DateField(auto_now_add=True)
    date = models.DateField(auto_now_add=False)
    country_code = models.CharField(max_length=2, blank=True, default='')
    temperature = models.CharField(max_length=4, blank=True, default='')
