# pythonmanage.pyweather_forecast 2021-26-05 CZ
from django.core.management.base import BaseCommand
from weatherForecast.services import WeatherApi
from django.conf import settings
import re
from datetime import datetime
import argparse

def valid_country(country_code):
        if country_code not in settings.WEATHER_API_ALLOWED_COUNTRIES:
            msg = "not a valid country"
            raise argparse.ArgumentTypeError(msg)
        else:
            return country_code

class Command(BaseCommand):
    help = 'Get weather conditions'

    def add_arguments(self, parser):
        parser.add_argument(
            'date',
            nargs='+',
            type=lambda d: datetime.strptime(d, '%Y-%m-%d').strftime('%Y-%m-%d'),
        )
        parser.add_argument(
            'country_code',
            nargs='+',
            type=valid_country,
            help=str(settings.WEATHER_API_ALLOWED_COUNTRIES),
        )
    
    def handle(self, **options):
        date = options['date'][0]
        country_code = options['country_code'][0]
        temperature = WeatherApi.get_temperature(country_code, date)

        if temperature == False:
            self.stdout.write(self.style.ERROR('Something went wrong check logs'))

        self.stdout.write(self.style.SUCCESS('weather: "%s"' % temperature))