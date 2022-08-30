from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('info/',views.info, name='info'),
    path('new_url/', views.new_URL, name='new_url'),
    path('delete/<id>/',views.delete_city,name='delete_city'),

]