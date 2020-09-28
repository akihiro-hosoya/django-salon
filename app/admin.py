from django.contrib import admin
from .models import Salon, Stylist, Booking

# Register your models here.
admin.site.register(Salon)
admin.site.register(Stylist)
admin.site.register(Booking)