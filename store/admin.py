from django.contrib import admin
from .models import Products,Categories,Cart,Wishlist,Order,OrderItem,Profile

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)