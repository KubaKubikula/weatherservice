import logging
import requests
from weatherForecast.models import Weather
from weatherForecast.serializers import WeatherSerializer

logger = logging.getLogger("djangologer")

class WeatherApi:
    API_KEY = ""
    
    def apiCall(countryCode, date):
        if countryCode == 'CZ':
            city = 'Prague'
        elif countryCode == 'SK':
            city = 'Bratislava'
        else:
            city = 'London'
        
        response = requests.get(
            'http://api.weatherapi.com/v1/history.json?key=' +
            WeatherApi.API_KEY +
            '&q=' +
            city +
            '&date=' +
            date)
        
        if response.status_code != 200:
            logger.warning(response.json())
            return False
        
        json = response.json()
        return json["forecast"]['forecastday'][0]['day']['avgtemp_c']

    def getTemperature(country_code, date):
        try:
            temperature = float(
                Weather.objects.get(
                    countryCode=country_code,
                    date=date).temperature)
        except Weather.DoesNotExist:
            temperature = WeatherApi.apiCall(
                countryCode=country_code, date=date)

            if temperature is int or float:
                data = {
                    "countryCode": country_code,
                    "date": date,
                    "temperature": temperature
                }
                serializer = WeatherSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return False
            else:
                return False

        if(temperature > 20):
            return "good"
        if(temperature < 20 and temperature > 10):
            return "soso"
        else:
            return "bad"