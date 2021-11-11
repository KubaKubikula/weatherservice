# pythonmanage.pyweather_forecast 2021-26-05 CZ
from django.core.management.base import BaseCommand
from weatherForecast.services import WeatherApi
from django.conf import settings
from datetime import datetime
import argparse
import re

def valid_country(country_code):
        if country_code not in settings.WEATHER_API_ALLOWED_COUNTRIES:
            msg = 'not a valid country'
            raise argparse.ArgumentTypeError(msg)
        else:
            return country_code

def valid_dateformat(date):
        if re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date) is None:
            msg = 'date format has to be {YYYY-MM-DD}'
            raise argparse.ArgumentTypeError(msg)
        else:
            return date

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'date',
            nargs='+',
            type=valid_dateformat,
        )
        parser.add_argument(
            'country_code',
            nargs='+',
            type=valid_country,
        )
    
    def handle(self, **options):
        date = options['date'][0]
        country_code = options['country_code'][0]
        temperature = WeatherApi.get_temperature(country_code, date)

        if temperature == False:
            self.stdout.write(self.style.ERROR('Something went wrong check logs'))

        self.stdout.write(self.style.SUCCESS('{"forecast": "%s"}' % temperature))