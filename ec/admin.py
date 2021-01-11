from django.contrib import admin
from ec.models import Item, OrderItem, Order, Payment, Purchaser

# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Purchaser)