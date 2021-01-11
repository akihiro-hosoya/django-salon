from django.contrib import admin
from .models import Salon, Stylist, Booking, News, StyleCategory, Style, MenuCategory, Menu, User, Staff

# Register your models here.
admin.site.register(Salon)
admin.site.register(Stylist)
admin.site.register(Booking)
admin.site.register(News)
admin.site.register(StyleCategory)
admin.site.register(Style)
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(User)
admin.site.register(Staff)