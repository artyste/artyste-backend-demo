from django.contrib import admin
from .models import UserAccount, card
# Register your models here.


class cardInline(admin.StackedInline):
    model = card
    extra = 0

@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups','user_permissions',)
    inlines = [cardInline,]