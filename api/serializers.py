from rest_framework import serializers
from art.models import gallery

class gallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = '__all__'