from rest_framework import serializers
from weatherForecast.models import Weather
import logging
import json

class WeatherSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Weather
        db_table = 'weather'
        fields = ['id', 'created']
    
    def save(self):

        return True