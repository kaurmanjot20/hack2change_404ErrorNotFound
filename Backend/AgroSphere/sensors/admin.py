from django.contrib import admin
from .models import SensorData

# Register your models here.

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'dht_humidity', 'dht_temperature', 'soil_moisture', 'rain', 'light', 'analog_temperature', 'digital_temperature')
    list_filter = ('timestamp',)
    search_fields = ('timestamp',)
    ordering = ('-timestamp',)

admin.site.register(SensorData, SensorDataAdmin)