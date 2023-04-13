# Generated by Django 4.0.4 on 2022-05-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_remove_product_is_available_remove_product_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='photos/products/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
