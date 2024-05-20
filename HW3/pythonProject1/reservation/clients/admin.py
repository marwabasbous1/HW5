from django.contrib import admin

# Register your models here.
from .models import Client, ClientType, Product, Order

admin.site.register(ClientType)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
