# Generated by Django 5.0.7 on 2024-07-26 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0002_alter_sensordata_analog_temperature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
