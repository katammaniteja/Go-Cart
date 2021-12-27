from django.contrib import admin
from .models import Products,Categories,Cart,Wishlist

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Wishlist)