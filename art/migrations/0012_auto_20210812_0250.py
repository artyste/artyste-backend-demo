# Generated by Django 3.2.5 on 2021-08-12 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0011_auto_20210812_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='product',
            field=models.ManyToManyField(related_name='galleryproducts', to='art.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='gallery', to='art.gallery'),
        ),
    ]