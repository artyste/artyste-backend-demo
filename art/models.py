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


class virtualGallery(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='virtualGallery/', blank=True, null=True)

class gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    imglogo = models.ImageField('Imagem Logo', upload_to=gallery_directory_path, blank=True, null=True)
    imgbabner = models.ImageField('Imagem Banner', upload_to=gallery_directory_path, blank=True, null=True)
    virtual = models.ForeignKey(virtualGallery, on_delete=models.DO_NOTHING, null=True)
    admin = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)

    def extra_virtualFile(self):
        try:
            return self.virtual.file
        except:
            return ''

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def __str__(self):
        return self.name



class product(models.Model):
    FIAT_STATUS = [
        (0, 'Ethereum'),
        (1, 'U.S. Dollar'),
        (2, 'Solana'),
    ]
    TYPE_STATUS = [
        (0, 'Digital'),
        (1, 'Physical'),
    ]
    MINTING_STATUS = [
        (0, 'No Minted'),
        (1, 'Subimited to Blockchain'),
        (2, 'Minted'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.IntegerField('Typw', choices=TYPE_STATUS, default=0)
    owner = models.ForeignKey(UserAccount, related_name='owner', on_delete=models.SET_NULL, blank=True, null=True)
    artist = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
    gallery = models.ForeignKey(gallery, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(default=0)
    fiat = models.IntegerField('Fiat', choices=FIAT_STATUS, default=0)

    fileimage = models.FileField(upload_to=artist_directory_path, blank=True, null=True)
    filehash = models.CharField('cid', max_length=255, blank=True, null=True)
    filemeta = models.CharField('meta cid', max_length=255, blank=True, null=True)

    mintingstatus = models.IntegerField('Minting Status', choices=MINTING_STATUS, default=0)
    mintingtx = models.CharField('Minting Transaction', max_length=255, blank=True, null=True)
    mintinghash = models.CharField('Minting Hash', max_length=255, blank=True, null=True)
    mintingid = models.IntegerField('Minting Id', blank=True, null=True)

    wallet = models.CharField(max_length=255, blank=True, null=True)
    royalty = models.FloatField(default=0)

    visible = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def extra_artistFirstName(self):
        try:
            return self.artist.first_name
        except:
            return ''

    def extra_artistLastName(self):
        try:
            return self.artist.last_name
        except:
            return ''

    def __str__(self):
        return self.title


class transaction(models.Model):
    FIAT_STATUS = [
        (0, 'Ethereum'),
        (1, 'U.S. Dollar'),
    ]
    GATE_STATUS = [
        (0, 'MetaMask'),
        (1, 'Circle CreditCard'),
    ]
    TRANS_STATUS = [
        (0, 'Created'),
        (1, 'Succeeded'),
        (2, 'Fail'),
        (3, 'Pending'),
    ]
    product = models.ForeignKey(product, on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField('Status', choices=TRANS_STATUS, default=0)
    fiat = models.IntegerField('Fiat', choices=FIAT_STATUS, default=0)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    txid = models.CharField('Transaction ID', max_length=255, blank=True, null=True)
    gateway = models.IntegerField('Payment Gateway', choices=GATE_STATUS, default=0)

    def __str__(self):
        return self.product.title

class collection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
