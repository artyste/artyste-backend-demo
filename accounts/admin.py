from django.contrib import admin
from .models import UserAccount
# Register your models here.
@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups','user_permissions',)