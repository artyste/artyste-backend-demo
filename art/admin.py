from django.contrib import admin
from .models import gallery, collection, product
# Register your models here.


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    pass

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    pass
