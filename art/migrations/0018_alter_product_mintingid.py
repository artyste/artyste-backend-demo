# Generated by Django 3.2.5 on 2021-08-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0017_product_mintingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mintingid',
            field=models.IntegerField(blank=True, null=True, verbose_name='Minting Id'),
        ),
    ]
