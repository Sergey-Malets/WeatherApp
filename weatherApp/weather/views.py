from django.shortcuts import render
import requests


def index(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    city = 'London'
    res = requests.get(url.format(city))
    res2 = requests.get(url.format('Minsk'))

    print(res.text)
    print(res2.text)

    return render(request, 'weather/index.html')

def new_URL(request):
    return render(request, "weather/new_url.html")

def index_2(request):
    return render(request, 'weather/index_2.html')
