from django.db import models
from accounts.models import UserAccount
from django.urls import reverse
from django.utils import timezone
from datetime import datetime
import os

def artist_directory_path(instance, filename):
    timenow = int(datetime.timestamp(timezone.now()))
    artistid = instance.artist.id
    extention = os.path.splitext(filename)
    return 'documents/{0}/{1}'.format(artistid, str(artistid) + '_' + str(timenow) + extention[-1])


def gallery_directory_path(instance, filename):
    timenow = int(datetime.timestamp(timezone.now()))
    extention = os.path.splitext(filename)
    return 'galleries/{0}/{1}'.format(str(instance.id), str(instance.id) + '_' + str(timenow) + extention[-1])


class product(models.Model):
    FIAT_STATUS = [
        (0, 'Ethereum'),
        (1, 'U.S. Dollar'),
    ]
    MINTING_STATUS = [
        (0, 'No Minted'),
        (1, 'Subimited to Blockchain'),
        (2, 'Minted'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING, related_name='Artist')
    curator = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING, related_name='Curator', blank=True, null=True)
    price = models.FloatField(default=0)
    fiat = models.IntegerField('Fiat', choices=FIAT_STATUS, default=0)

    fileimage = models.FileField(upload_to=artist_directory_path, blank=True, null=True)
    filehash = models.CharField('cid', max_length=255, blank=True, null=True)

    mintingstatus = models.IntegerField('Minting Status', choices=MINTING_STATUS, default=0)
    mintingtx = models.CharField('Minting Transaction', max_length=255, blank=True, null=True)
    mintinghash = models.CharField('Minting Hash', max_length=255, blank=True, null=True)

    wallet = models.CharField(max_length=255, blank=True, null=True)
    royalty = models.FloatField(default=0)

    visible = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class collection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    imglogo = models.ImageField('Imagem Logo', upload_to=gallery_directory_path, blank=True, null=True)
    imgbabner = models.ImageField('Imagem Banner', upload_to=gallery_directory_path, blank=True, null=True)
    admin = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(product, blank=True)

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def __str__(self):
        return self.name