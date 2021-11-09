import requests

class WeaterApi:
    
    API_KEY = "test"

    def apiCall(self, countryCode, date):
        #response = requests.get('http://api.weatherapi.com/v1/current.json?key=' + self.API_KEY + '&q=London&aqi=no')
        return 15