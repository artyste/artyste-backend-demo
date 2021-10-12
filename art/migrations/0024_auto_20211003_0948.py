# Generated by Django 3.2.5 on 2021-10-03 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0023_alter_product_fiat'),
    ]

    operations = [
        migrations.CreateModel(
            name='virtualGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fileimage', models.FileField(blank=True, null=True, upload_to='virtualGallery/')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='virtual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='art.virtualgallery'),
        ),
    ]
