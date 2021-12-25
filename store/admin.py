from django.contrib import admin
from .models import Products,Categories

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)