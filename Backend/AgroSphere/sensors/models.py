from django.db import models

# Create your models here.
import datetime

class SensorData(models.Model):
    dht_humidity = models.FloatField(null=True, blank=True)
    dht_temperature = models.FloatField(null=True, blank=True)
    soil_moisture = models.FloatField(null=True, blank=True)
    rain = models.FloatField(null=True, blank=True)
    light = models.FloatField(null=True, blank=True)
    analog_temperature = models.FloatField(null=True, blank=True)
    digital_temperature = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    
    def __str__(self):
        return str(self.timestamp)