import logging
import requests
from weatherForecast.models import Weather
from weatherForecast.serializers import WeatherSerializer
from django.conf import settings

logger = logging.getLogger('djangologer')

class WeatherApi:

    def api_call(country_code, date):
        if country_code == 'CZ':
            city = 'Prague'
        elif country_code == 'SK':
            city = 'Bratislava'
        else:
            city = 'London'
        
        response = requests.get(
            settings.WEATHER_API_URL +
            '?key=' +
            settings.WEATHER_API_KEY +
            '&q=' +
            city +
            '&date=' +
            date)
        
        if response.status_code != 200:
            logger.warning(response.json())
            return False
        
        json = response.json()
        return json['forecast']['forecastday'][0]['day']['avgtemp_c']

    def get_temperature(country_code, date):
        
        WeatherItem = Weather.objects.filter(country_code=country_code,date=date).first()
        #logger.warning(str(WeatherItem))

        if WeatherItem == None:
            temperature = WeatherApi.api_call(
                country_code=country_code, date=date)

            if temperature is int or float:
                data = {
                    'country_code': country_code,
                    'date': date,
                    'temperature': temperature
                }
                serializer = WeatherSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return False
            else:
                return False
        else:
            temperature = float(WeatherItem.temperature)

        if(temperature > 20):
            return 'good'
        if(temperature <= 20 and temperature >= 10):
            return 'soso'
        else:
            return 'bad'