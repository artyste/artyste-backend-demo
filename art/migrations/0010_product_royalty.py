# Generated by Django 3.2.5 on 2021-08-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0009_alter_product_fileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='royalty',
            field=models.FloatField(default=0),
        ),
    ]
