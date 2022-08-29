from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('home/',views.index_3, name='home_2'),
    path('new_url/', views.new_URL, name='new_url'),
    path('delete/<city_name>/',views.delete_city,name='delete_city'),

]