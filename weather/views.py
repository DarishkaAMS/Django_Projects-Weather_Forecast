import requests
from django.shortcuts import render

from .models import City
# Create your views here.


def index_view(request):
    app_id = "7b06996e671b504dcc4a6e2ed52111ed"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id
    city = "London"

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        response = requests.get(url.format(city)).json()

        city_info = {
            'city': city.name,
            'temp': response['main']['temp'],
            'feels_like': response['main']['feels_like'],
            'clouds': response['clouds']['all'],
            'icon': response['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {'all_info': all_cities}

    return render(request, 'weather/index.html', context)
