# Generated by Django 3.0.5 on 2021-10-04 06:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WatchApp', '0007_auto_20210930_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(help_text='If the color not available in the list, use the above color form to add color', on_delete=django.db.models.deletion.PROTECT, to='WatchApp.Color', verbose_name='Watch Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 10, 4, 6, 23, 2, 809477, tzinfo=utc)),
        ),
    ]
