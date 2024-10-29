from django.contrib import admin
from .models import RideRequest, Transaction

admin.site.register(RideRequest)
admin.site.register(Transaction)