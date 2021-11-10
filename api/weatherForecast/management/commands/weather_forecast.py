# pythonmanage.pyweather_forecast 2021-26-05 CZ
from django.core.management.base import BaseCommand
from weatherForecast.services import WeatherApi

class Command(BaseCommand):
    help = 'Get weather conditions'

    def add_arguments(self, parser):
        parser.add_argument('date', nargs='+')
        parser.add_argument('country_code', nargs='+')

    def handle(self):
        temperature = WeatherApi.get_temperature()
        if temperature == False:
            self.stdout.write(self.style.ERROR('Something went wrong check logs'))

        self.stdout.write(self.style.SUCCESS('weather: "%s"' % temperature))