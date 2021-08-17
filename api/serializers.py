from rest_framework import serializers
from art.models import gallery, product

class gallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = '__all__'

class productSerializers(serializers.ModelSerializer):
    my_field2 = serializers.ReadOnlyField(source='my_field')

    class Meta:
        model = product
        fields = '__all__'
