from django.db import models

class Sensor(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    z = models.IntegerField(default=0)
    result = models.CharField(max_length=100)
# Create your models here.
