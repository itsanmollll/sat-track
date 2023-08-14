# Generated by Django 4.1.4 on 2023-08-14 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0016_tle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tle',
            name='date_added',
        ),
        migrations.AddField(
            model_name='tle',
            name='epoch_date',
            field=models.DateTimeField(default=datetime.datetime(2000, 2, 2, 2, 2, 2, 2), verbose_name='Epoch Date'),
        ),
    ]
