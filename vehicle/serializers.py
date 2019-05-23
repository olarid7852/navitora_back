from rest_framework.serializers import ModelSerializer
from .models import Vehicle, VehicleLocation

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class VehicleLocationSerializer(ModelSerializer):
    class Meta:
        model = VehicleLocation
        fields = '__all__'