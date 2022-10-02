from rest_framework import serializers
from searches.models import TouristDestination

class TouristDestinationSerializers(serializers.ModelSerializer):
    class Meta:
        model = TouristDestination
        fields = '__all__'