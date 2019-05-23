from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, response
from rest_framework.decorators import action
from .models import Vehicle, VehicleLocation
from .serializers import VehicleSerializer, VehicleLocationSerializer
import requests

# Create your views here.

class VehicleViewSet(ModelViewSet):
    model = Vehicle
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        data["user"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

class VehicleLocationViewSet(ModelViewSet):
    model = VehicleLocation
    queryset = VehicleLocation.objects.all()
    serializer_class = VehicleLocationSerializer

    @action(detail=False, methods=["GET"])
    def listgeo(self, request, *args, **kwargs):
        locations = [
        {"lat": -31.563910, "lng": 147.154312},
        {"lat": -33.718234, "lng": 150.363181},
        {"lat": -33.727111, "lng": 150.371124},
        {"lat": -33.848588, "lng": 151.209834},
        {"lat": -33.851702, "lng": 151.216968},
        {"lat": -34.671264, "lng": 150.863657},
        {"lat": -35.304724, "lng": 148.662905},
        {"lat": -36.817685, "lng": 175.699196},
        {"lat": -36.828611, "lng": 175.790222},
        {"lat": -37.750000, "lng": 145.116667},
        {"lat": -37.759859, "lng": 145.128708},
        {"lat": -37.765015, "lng": 145.133858},
        {"lat": -37.770104, "lng": 145.143299},
        {"lat": -37.773700, "lng": 145.145187},
        {"lat": -37.774785, "lng": 145.137978},
        {"lat": -37.819616, "lng": 144.968119},
        {"lat": -38.330766, "lng": 144.695692},
        {"lat": -39.927193, "lng": 175.053218},
        {"lat": -41.330162, "lng": 174.865694},
        {"lat": -42.734358, "lng": 147.439506},
        {"lat": -42.734358, "lng": 147.501315},
        {"lat": -42.735258, "lng": 147.438000},
        {"lat": -43.999792, "lng": 170.463352}
        ]
        return response.Response(locations)

    @action(detail=False, methods=["GET"])
    def listroute(self, request, *args, **kwargs):
        routes = "https://roads.googleapis.com/v1/snapToRoads?path=-35.27801,149.12958|-35.28032,149.12907|-35.28099,149.12929|-35.28144,149.12984|-35.28194,149.13003|-35.28282,149.12956|-35.28302,149.12881|-35.28473,149.12836&interpolate=true&key=AIzaSyBYCfS1nBZ-Ff6CRZ87Wclu6_ckGFRhlAQ"
        req = requests.get(routes)
        return response.Response(req.json())

    @action(detail=False, methods=["POST"])
    def creater(self, request, *args, **kwargs):
        return super(ModelViewSet, self).create(request, *args, **kwargs)
