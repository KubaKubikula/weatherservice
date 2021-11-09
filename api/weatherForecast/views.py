from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weatherForecast.models import Weather
from weatherForecast.serializers import WeatherSerializer
from weatherForecast.services import WeatherApi
import re
import logging

# Create your views here.
@csrf_exempt
def weather_detail(request):
    if request.method == 'GET':
        date = request.GET.get('date','')
        country_code = request.GET.get('country_code','')
        if date == "" or re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date) or country_code not in ['CZ','SK','UK']:
            return JsonResponse({"error": "wrong input data - need country_code={XX} - possible values CZ, SK or UK and date{YYYY-MM-DD}"}, status=400)    
        
        try:
            temperature = float(Weather.objects.get(countryCode=country_code, date=date).temperature)
        except Weather.DoesNotExist:
            temperature = WeatherApi.apiCall(countryCode=country_code, date=date)
            
            if type(temperature) == int or float:
                data = {"countryCode": country_code, "date": date, "temperature" : temperature}
                serializer = WeatherSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return JsonResponse({"error": "saving data error"}, status=400)
            else:
                return JsonResponse({"error": "api call error"}, status=400)

        if temperature > 20:
            return JsonResponse({"forecast": "good"}, status=200)
        elif temperature < 20 and temperature > 10:
            return JsonResponse({"forecast": "soso"}, status=200)
        else:
            return JsonResponse({"forecast": "bad"}, status=200)
        