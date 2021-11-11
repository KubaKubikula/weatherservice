# pythonmanage.pyweather_forecast 2021-26-05 CZ
from django.core.management.base import BaseCommand
from weatherForecast.services import WeatherApi
import re

class Command(BaseCommand):
    help = 'Get weather conditions'

    def add_arguments(self, parser):
        parser.add_argument('date', nargs='+')
        parser.add_argument('country_code', nargs='+')

    def handle(self, *args, **options):
        date = options['date'][0]
        country_code = options['country_code'][0]

        if date == "" or re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date) is None or country_code not in ['CZ','SK','UK']:
            self.stdout.write(self.style.ERROR('wrong input data - need country_code={XX} - possible values CZ, SK or UK and date{YYYY-MM-DD}'))
        else:
            temperature = WeatherApi.get_temperature(country_code, date)

            if temperature == False:
                self.stdout.write(self.style.ERROR('Something went wrong check logs'))

            self.stdout.write(self.style.SUCCESS('weather: "%s"' % temperature))