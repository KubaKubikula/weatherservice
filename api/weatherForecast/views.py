import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from weatherForecast.services import WeatherApi
from django.conf import settings
import re

logger = logging.getLogger('djangologer')

@csrf_exempt
def weather_detail(request):
    if request.method == 'GET':
        date = request.GET.get('date', '')
        country_code = request.GET.get('country_code', '')
        if date == "" or re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date) is None or country_code not in settings.WEATHER_API_ALLOWED_COUNTRIES:
            logger.warning("wrong input data format")
            return JsonResponse(
                {'error': 'wrong input data - need country_code={XX} - possible values CZ, SK or UK and date{YYYY-MM-DD}'}, status=400)

        temperature = WeatherApi.get_temperature(country_code=country_code, date=date)

        if temperature == False:
            return JsonResponse({'error': 'Something went wrong check warning.log for more details'}, status=500)
        
        return JsonResponse({'weather': temperature}, status=200)
        
