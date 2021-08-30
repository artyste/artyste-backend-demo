# Generated by Django 3.2.5 on 2021-08-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0020_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='gateway',
            field=models.IntegerField(choices=[(0, 'MetaMask'), (1, 'Circle CreditCard')], default=0, verbose_name='Payment Gateway'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='txid',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Transaction ID'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Succeeded'), (2, 'Fail'), (3, 'Pending')], default=0, verbose_name='Status'),
        ),
    ]
