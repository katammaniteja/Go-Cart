from django.contrib import admin
from .models import Products,Categories,Cart

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Cart)