from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cites = []

    for city in cities:
        res = requests.get(url.format(city)).json()

        city_info = {
            'city': city,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cites.append(city_info)

    context = {
        'all_info': all_cites,
        'form': form,
    }

    return render(request, 'weather/index.html', context)

def new_URL(request):
    return render(request, "weather/new_url.html")

def index_3(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cites = []

    for city in cities:
        res = requests.get(url.format(city)).json()

        city_info = {
            'city': city,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon'],
            'feels_like': res['main']['feels_like'],
            'wind': res['wind']['speed'],
            "description": res['weather'][0]['description'],
            'country': res['sys']['country']

        }
        all_cites.append(city_info)

    context = {
        'all_info': all_cites,
        'form': form,
    }

    return render(request, 'weather/index_3.html', context)
