from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OpenWeatherMap(models.Model):
    appid = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.url