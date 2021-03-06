# Generated by Django 3.0.5 on 2021-10-04 07:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WatchApp', '0008_auto_20211004_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(help_text='If the brand not available in the list, use the above brand form to add brand', on_delete=django.db.models.deletion.PROTECT, to='WatchApp.Brand', verbose_name='Watch Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 4, 7, 58, 18, 363295, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(help_text='If the size not available in the list, use the above size form to add size', on_delete=django.db.models.deletion.PROTECT, to='WatchApp.Size', verbose_name='Watch Size'),
        ),
    ]
