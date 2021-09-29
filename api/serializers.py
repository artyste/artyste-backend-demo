from rest_framework import serializers
from art.models import gallery, product

class gallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = '__all__'

class productSerializers(serializers.ModelSerializer):
    artistFirstName = serializers.ReadOnlyField(source='extra_artistFirstName')
    artistLastName = serializers.ReadOnlyField(source='extra_artistLastName')

    class Meta:
        model = product
        fields = '__all__'
        read_only_fields = (
            'artistFirstName', 'artistLastName',
        )
