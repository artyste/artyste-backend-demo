# Generated by Django 3.2.5 on 2021-08-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0014_auto_20210813_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]