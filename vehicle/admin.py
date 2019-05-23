from django.contrib import admin
from .models import Vehicle, VehicleLocation

# from allauth.account.models import EmailAddress
from allauth.account.models import EmailConfirmation
# from allauth.account.models import SocialAccount
# from allauth.account.models import SocialApp
# from allauth.account.models import SocialToken

# Register your models here.
# admin.site.register(EmailAddress)
admin.site.register(EmailConfirmation)
admin.site.register(Vehicle)
admin.site.register(VehicleLocation)
# admin.site.register(SocialAccount)
# admin.site.register(SocialApp)
# admin.site.register(SocialToken)
