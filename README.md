# weatherservice


Videotutorial HERE https://www.youtube.com/watch?v=8SBBsSPaREg


Instalation
--------------

git clone git@github.com:KubaKubikula/weatherservice.git

cd weatherservice

docker-compose up

#(enter django container and run migrations)#

  docker exec -it weatherservice_django_1 /bin/bash
  python manage.py migrate


setup /api/settings.py WEATHER_API_KEY (here you have to put api key from your https://www.weatherapi.com/my/)

thats it than it should be possible to:

http://127.0.0.1:8000/weather-forecast/?date=2021-11-05&country_code=CZ

and also run command in docker container
python manage.py weather_forecast 2021-11-05 CZ

Adminer is available on 

http://localhost:8080 

'ENGINE': 'django.db.backends.postgresql',
'NAME': 'postgres',
'USER': 'postgres',
'HOST': 'db',
'PASSWORD': 'postgres'
    
