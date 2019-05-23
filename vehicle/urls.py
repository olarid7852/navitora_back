from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'vehicle'
router = routers.DefaultRouter()
# router.register('', views.ServiceView)
router.register('', views.VehicleViewSet)
router.register('location', views.VehicleLocationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
