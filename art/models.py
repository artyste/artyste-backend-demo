from django.db import models
from accounts.models import UserAccount

class product(models.Model):
    MINTING_STATUS = [
        (0, 'No Minted'),
        (1, 'Subimited to Blockchain'),
        (2, 'Minted'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    artist = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    price = models.FloatField(default=0)
    file = models.CharField(max_length=255, blank=True, null=True)
    mintingstatus = models.IntegerField('Minting Status', choices=MINTING_STATUS, default=0)
    mintingtx = models.CharField('Minting Transaction', max_length=255, blank=True, null=True)
    mintinghash = models.CharField('Minting Hash', max_length=255, blank=True, null=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class collection(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(product, blank=True, null=True)

    def __str__(self):
        return self.name

class gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    admin = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    collection = models.ManyToManyField(collection, blank=True, null=True)

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def __str__(self):
        return self.name