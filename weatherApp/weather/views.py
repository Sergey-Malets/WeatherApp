from django.shortcuts import render
import requests


def index(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'London'
    res = requests.get(url.format(city)).json()
    res2 = requests.get(url.format('Minsk'))

    city_info={
        'city': city,
        'temp':res['main']['temp'],
    'icon': res['weather'][0]['icon']
    }
    context = {
        'info': city_info
    }

    return render(request, 'weather/index.html', context)

def new_URL(request):
    return render(request, "weather/new_url.html")

def index_2(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'London'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'feels_like': res['main']['feels_like'],
        'wind': res['wind']['speed'],
    }
    context = {
        'info': city_info
    }

    return render(request, 'weather/index_2.html', context)
