from rest_framework import serializers
from apartments.models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('id', 'title', 'apartment_url', 'image_path', 'description',
                  'published')
