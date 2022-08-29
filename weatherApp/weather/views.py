from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.views.generic import ListView


class Home(ListView):
    model = City
    #по умолчанию нужен шаблон с путем: weather/City_list.html ,но мы пропишем путь к действующему index.html
    template_name = 'weather/index.html'
    context_object_name = 'cities' # отображает без данных с сайта OpenWeatherMap, нужно копнуть глубже
    extra_context = {'title':"Главная страница"} #можно передавать только статические(неизменяемые данные)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) #обращаемся к базовому класу ЛистВью и берем существующий контекст



def index(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    err_msg = ''
    message = ''
    message_class = ''

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_pcount = City.objects.filter(name=new_city).count()
            if existing_pcount == 0:
                res=requests.get(url.format(new_city)).json()
                if res['cod']==200:
                    form.save()
                else:
                    err_msg = 'Такого города нет в базе данных метеоцентра или проверьте правильность написания'
            else:
                err_msg = "Данный город уже добавлен"

        if err_msg:
            message = err_msg
            message_class = 'alert-danger'
        else:
            message = "Город добавлен"
            message_class='alert-success'

    form = CityForm

    cities = City.objects.all()
    all_cities=[]

    for city in cities:
        res = requests.get(url.format(city)).json()
        city_info = {
            'city': city,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
        'message':message,
        'message_class':message_class
    }
    return render(request, 'weather/index.html', context)

def delete_city(request,city_name):
    City.objects.get(name=city_name).delete()

    return redirect('home')


def new_URL(request):
    return render(request, "weather/new_url.html")

def index_3(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid

    cities = City.objects.all()
    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()
    form = CityForm

    all_cities = []

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
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
    }
    return render(request, 'weather/index_3.html', context)
