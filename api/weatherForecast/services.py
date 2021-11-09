import logging
import requests
from rest_framework.parsers import JSONParser
import json

class WeatherApi: 
    API_KEY = ""

    def apiCall(countryCode, date):
        
        if countryCode == 'CZ':
            city = 'Prague'
        elif countryCode == 'SK':
            city = 'Bratislava'
        else:
            city = 'London'

        response = requests.get('http://api.weatherapi.com/v1/history.json?key=' + WeatherApi.API_KEY + '&q=' + city + '&date=' + date)
        json = response.json()
        return json["forecast"]['forecastday'][0]['day']['avgtemp_c']