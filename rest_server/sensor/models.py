from django.db import models

class Sensor(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    def __str__(self):
        return self.x
# Create your models here.
