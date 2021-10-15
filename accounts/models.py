from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    nickname = models.CharField(max_length=255, unique=True, blank=True, null=True)
    avatar = models.ImageField('Avatar', upload_to='users/', blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    wallet_hash = models.CharField(max_length=255, blank=True, null=True)

    circle_walletId = models.CharField(max_length=255, blank=True, null=True)
    circle_entityId = models.CharField(max_length=255, blank=True, null=True)
    circle_chainETH = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField(null=True, blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

class card(models.Model):
    CARD_FLAG = [
        (0, 'Visa'),
        (1, 'Mastercard'),
    ]
    user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    cardid = models.CharField(max_length=255, blank=True, null=True)
    flag = models.IntegerField('Card Flag', choices=CARD_FLAG, default=0)
    last = models.CharField(max_length=32, blank=True, null=True)
    cvv = models.CharField(max_length=255, blank=True, null=True)
