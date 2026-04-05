from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
