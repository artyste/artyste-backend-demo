from django.db import models
from accounts.models import UserAccount


def user_directory_path(instance, filename):
    return 'documents/{0}/{1}'.format(instance.user.username, filename)


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

    fileimage = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    filehash = models.CharField(max_length=255, blank=True, null=True)

    mintingstatus = models.IntegerField('Minting Status', choices=MINTING_STATUS, default=0)
    mintingtx = models.CharField('Minting Transaction', max_length=255, blank=True, null=True)
    mintinghash = models.CharField('Minting Hash', max_length=255, blank=True, null=True)

    wallet = models.CharField(max_length=255, blank=True, null=True)

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
    admin = models.ForeignKey(UserAccount, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField(product, blank=True)

    def get_absolute_url(self):
        return '/%s/' % self.slug

    def __str__(self):
        return self.name