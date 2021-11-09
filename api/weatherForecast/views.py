from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weatherForecast.models import Weather
from weatherForecast.serializers import WeatherSerializer
from weatherForecast.services import WeaterApi
import logging

# Create your views here.
@csrf_exempt
def weather_detail(request):
    if request.method == 'GET':
        data = {"countryCode":"CZ", "date": "2021-11-9"}

        temperature = Weather.objects.get(countryCode=data.countryCode, date=data.date)
        
        if temperature == False:
            temperature = WeaterApi.apiCall(countryCode=data.countryCode, date=data.date)
            
            if type(temperature) == int or float:
                data = {"countryCode":"CZ", "date": "2021-11-9", "temperature" : temperature}
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
        