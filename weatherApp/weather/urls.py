from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='home'),
    path('home/',views.index_2, name='home_2'),
    path('new_url/', views.new_URL, name='new_url')

]