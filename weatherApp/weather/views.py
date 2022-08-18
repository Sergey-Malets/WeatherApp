from django.shortcuts import render

def index(request):
    return render(request, 'weather/index.html')

def new_URL(request):
    return render(request, "weather/new_url.html")

def index_2(request):
    return render(request, 'weather/index_2.html')
