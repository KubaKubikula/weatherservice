from django.db import models

class Weather(models.Model):
    created = models.DateTimeField(auto_now_add=True)
