from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)
    temperature = models.DecimalField(max_digits=8, decimal_places=2)
    wind = models.DecimalField(max_digits=8, decimal_places=2)
    icon = models.CharField(max_length=10)
    feels_like = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class OpenWeatherMap(models.Model):
    appid = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.url