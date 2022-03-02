import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ecommerce.settings')
import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        funame=faker.name()
        fupass=str(randint(10000000, 20000000))
        user =User.objects.create_user(username=funame,password=fupass)
        user.save()
populate(100)