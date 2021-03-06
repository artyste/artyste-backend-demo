# Generated by Django 3.2.5 on 2021-08-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_auto_20210809_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='products',
            field=models.ManyToManyField(blank=True, to='art.product'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='collection',
            field=models.ManyToManyField(blank=True, to='art.collection'),
        ),
    ]
