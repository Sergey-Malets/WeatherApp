from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name='home'),
    path('new_url/', views.new_URL, name='new_url')

]