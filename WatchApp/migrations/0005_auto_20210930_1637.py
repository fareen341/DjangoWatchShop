# Generated by Django 3.0.5 on 2021-09-30 11:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('WatchApp', '0004_auto_20210930_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(help_text='Add watch brand', max_length=30, verbose_name='Watch Brand'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.CharField(help_text='Add watch color', max_length=30, unique=True, verbose_name='Watch Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(help_text='If the brand not available in the list, use the above brand form to add brand', on_delete=django.db.models.deletion.CASCADE, to='WatchApp.Brand', verbose_name='Watch Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(help_text='If the color not available in the list, use the above color form to add color', on_delete=django.db.models.deletion.CASCADE, to='WatchApp.Color', verbose_name='Watch Color'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 30, 11, 7, 58, 465755, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_on_men_section',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='No', help_text="Select yes if you want this product to be displayed on men's menu section", max_length=100, verbose_name="Display on men's watches menu?"),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_on_offer_section',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='No', help_text='If this product is on sale, select yes if you want this porduct to be display on the sale section', max_length=100, verbose_name='Display on sale selction?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_on_women_section',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='No', help_text="Select yes if you want this product to be displayed on women's menu section", max_length=100, verbose_name="Display on women's watches menu?"),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_product',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', help_text='If this is selected as yes the product will be visible on the product page, please select yes if you want this product to be display on product page', max_length=100, verbose_name='Display this product on product page?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='featured_product',
            field=models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='No', help_text='Select yes if you want this product to be displayed on featured product section', max_length=100, verbose_name='Featured product?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_desc',
            field=models.TextField(default='none', max_length=200, verbose_name='Product Description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_group_name',
            field=models.CharField(help_text='Note: The group name and product color should be unique', max_length=30, verbose_name='Product group name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(help_text="This is display image, it'll be visible on the product page", upload_to='images', verbose_name='Display Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img1',
            field=models.ImageField(default='none', help_text="Product's side image", upload_to='images', verbose_name='Side Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(default='none', help_text="Product's side image", upload_to='images', verbose_name='Side Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img3',
            field=models.ImageField(default='none', help_text="Product's side image", upload_to='images', verbose_name='Side Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_last_date',
            field=models.DateField(blank=True, help_text='After the sale last date product will show the regular price', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(help_text='If the size not available in the list, use the above size form to add size', on_delete=django.db.models.deletion.CASCADE, to='WatchApp.Size', verbose_name='Watch Size'),
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(help_text='Add watch size', max_length=30, verbose_name='Watch Size'),
        ),
    ]
