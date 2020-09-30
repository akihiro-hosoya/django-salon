from django.contrib import admin
from .models import Salon, Stylist, Booking, News, StyleCategory, Style, MenuCategory, Menu

# Register your models here.
admin.site.register(Salon)
admin.site.register(Stylist)
admin.site.register(Booking)
admin.site.register(News)
admin.site.register(StyleCategory)
admin.site.register(Style)
admin.site.register(MenuCategory)
admin.site.register(Menu)