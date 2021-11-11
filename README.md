# weatherservice


Videotutorial HERE https://www.youtube.com/watch?v=8SBBsSPaREg


Instalation
--------------
1) git clone git@github.com:KubaKubikula/weatherservice.git
2) cd weatherservice
3) docker-compose up

Enter django container and run migrations (and add api key)
--------------
4) docker exec -it weatherservice_django_1 /bin/bash 
5) python manage.py migrate
6) in /api/settings.py WEATHER_API_KEY (here you have to put api key from your https://www.weatherapi.com/my/) 

Usage
---------------
http://127.0.0.1:8000/weather-forecast/?date=2021-11-05&country_code=CZ

And also run command in docker container
---------------
python manage.py weather_forecast 2021-11-05 CZ

Adminer is available on 
---------------
http://localhost:8080 

'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER': 'postgres',
'HOST': 'db',
'PASSWORD': 'postgres'
    
