# Generated by Django 3.0.5 on 2021-09-30 11:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WatchApp', '0006_auto_20210930_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(help_text='Add watch brand', max_length=30, unique=True, verbose_name='Watch Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 30, 11, 9, 8, 796075, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(help_text='Add watch size', max_length=30, unique=True, verbose_name='Watch Size'),
        ),
    ]
