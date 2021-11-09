from rest_framework import serializers
from weatherForecast.models import Weather

class WeatherSerializer(serializers.Serializer): 

    class Meta:
        model = Weather
        db_table = 'weather'
        fields = ['date', 'countryCode', 'created', 'temperature']


#tady to budu načítat z api