from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


# Create your models here.
CAR_TYPE_CHOICES = (('sm', 'Small Car'),)

class Vehicle(models.Model):
    user = models.ForeignKey(User, verbose_name=_("owner"), on_delete=models.CASCADE)
    model = models.CharField(_("Model name"), max_length=50)
    registration_no = models.CharField(_("Model number"), max_length=50)
    name = models.CharField(_("Name"), max_length=50)
    # type = models.CharField(_("type"), max_length=2, choices=CAR_TYPE_CHOICES)

class VehicleLocation(models.Model):
    vehicle = models.ForeignKey(Vehicle, verbose_name=_("Vehicle"), on_delete=models.CASCADE)
    time = models.TimeField(_("Time"), auto_now=False, auto_now_add=True)
    latitude = models.FloatField(_("Latitude"))
    longitude = models.FloatField(_("Longitude"))
