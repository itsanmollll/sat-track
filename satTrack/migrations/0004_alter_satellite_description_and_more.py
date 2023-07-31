# Generated by Django 4.1.4 on 2023-07-31 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satTrack', '0003_alter_satellite_last_tle_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='satellite',
            name='description',
            field=models.TextField(default='-', verbose_name='About Satellite'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='last_tle_update',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 19, 45, 40, 800804), editable=False, verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='launch_date',
            field=models.DateField(default=datetime.datetime(2023, 7, 31, 19, 45, 40, 800804), verbose_name='Launch Date'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='manufacturer',
            field=models.CharField(default='-', max_length=15, verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='orbit',
            field=models.CharField(default='-', max_length=20, verbose_name='Orbit Type'),
        ),
        migrations.AlterField(
            model_name='satellite',
            name='satellite_type',
            field=models.CharField(default='-', max_length=30, verbose_name='Satellite type'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='resolution_type',
            field=models.CharField(default='-', max_length=30, verbose_name='Resolution Type'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='tilting_type',
            field=models.CharField(default='-', max_length=20, verbose_name='Tilting Type'),
        ),
    ]