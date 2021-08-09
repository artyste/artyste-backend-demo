from django.contrib import admin
from .models import gallery, collection, product
# Register your models here.


@admin.register(product)
class productAdmin(admin.ModelAdmin):
    pass

@admin.register(collection)
class collectionAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    filter_horizontal = ('collection',)
