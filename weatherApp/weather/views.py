from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm
from django.views.generic import ListView


# class Home(ListView):
#     model = City
#     #по умолчанию нужен шаблон с путем: weather/City_list.html ,но мы пропишем путь к действующему index.html
#     template_name = 'weather/index.html'
#     context_object_name = 'cities' # отображает без данных с сайта OpenWeatherMap, нужно копнуть глубже
#     extra_context = {'title':"Главная страница"} #можно передавать только статические(неизменяемые данные)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs) #обращаемся к базовому класу ЛистВью и берем существующий контекст


def delete_city(request,id):
    City.objects.get(id=id).delete()

    return redirect('info')

def new_URL(request):
    return render(request, "weather/new_url.html")

def index(request):
    appid = "22157536b45f94e241c43cc5f22072da"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    err_msg = ''
    message = ''
    message_class = ''



    if (request.method == 'POST'):
        form = CityForm(request.POST)
        city = request.POST['name']
        res = requests.get(url.format(city)).json()
        if res['cod'] == 200:
            city_info = {
                'city': city,
                'temp': res['main']['temp'],
                'icon': res['weather'][0]['icon'],
                'feels_like': res['main']['feels_like'],
                'wind': res['wind']['speed'],
                "description": res['weather'][0]['description'],
                'country': res['sys']['country']
            }
            if form.is_valid():
                City.objects.create(name=city_info['city'],
                                    temperature=city_info['temp'],
                                    feels_like=city_info['feels_like'],
                                    wind=city_info['wind'],
                                    description=city_info['description'],
                                    country=city_info['country'],
                                    icon=city_info['icon'])
        else:
            err_msg = 'Такого города нет в базе данных метеоцентра или проверьте правильность написания'
    if err_msg:
        message = err_msg
        message_class = 'alert-danger'
    # else:
    #     message = "Город добавлен"
    #     message_class = 'alert-success'

    form = CityForm

    if City.objects.all():
        city = City.objects.latest('id')  # Возвращает последний объект в таблице на основе заданных полей
    else:
        city = []




    context = {
        'form': form,
        'info': city,
        'message': message,
        'message_class': message_class
    }

    return render(request, 'weather/index_3.html', context)

def info(request):
    cities = City.objects.order_by("-id")

    context= {
        'all_info':cities,
    }
    return render(request, 'weather/info.html', context)
