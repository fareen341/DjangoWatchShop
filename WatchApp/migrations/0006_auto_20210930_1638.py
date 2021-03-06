# Generated by Django 3.0.5 on 2021-09-30 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WatchApp', '0005_auto_20210930_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 30, 11, 8, 28, 668102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(max_length=200, verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(help_text="Product's side image", upload_to='images', verbose_name='Side Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(help_text="Product's side image", upload_to='images', verbose_name='Side Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(help_text="Product's side image", upload_to='images', verbose_name='Side Image'),
        ),
    ]
