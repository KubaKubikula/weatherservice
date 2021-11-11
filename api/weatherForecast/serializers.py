from rest_framework import serializers
from weatherForecast.models import Weather


class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        db_table = 'weather'
        fields = ['date', 'country_code', 'created', 'temperature']
