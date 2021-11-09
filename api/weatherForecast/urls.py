from django.urls import path, re_path
from weatherForecast import views

# GET /weather-forecast/?date={YYYY-MM-DD}&country_code={ISO_CODE_2}
urlpatterns = [
    path('weather-forecast/', views.weather_detail),
]