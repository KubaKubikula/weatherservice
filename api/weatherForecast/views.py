from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weatherForecast.models import Weather
from weatherForecast.serializers import WeatherSerializer
import logging

# Create your views here.
@csrf_exempt
def weather_detail(request):
    if request.method == 'GET':
        weather = Weather.objects.all()
        serializer = WeatherSerializer(weather, many=True)
        return JsonResponse(serializer.data, safe=False)