# Generated by Django 3.2.5 on 2021-10-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
