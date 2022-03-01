from django.db import models
import datetime
import os
from django.contrib.auth.models import User

# Create your models here.
def get_file_path(request,filename):
    return os.path.join('uploads/',filename)

class Categories(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description=models.TextField(max_length=1000,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(null=True,blank=True)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag=models.CharField(max_length=150,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_cart')
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

class Wishlist(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_wishlist')
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=150,null=False)
    lname=models.CharField(max_length=150,null=False)
    email=models.CharField(max_length=150,null=False)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pincode=models.CharField(max_length=150,null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True,blank=True)
    orderstatuses=(
        ("Pending","Pending"),
        ("Out for shipping","Out for shipping"),
        ("Delivered","Delivered")
    )
    status=models.CharField(max_length=150,choices=orderstatuses,default="Pending")
    message=models.TextField(null=True,blank=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.id,self.tracking_no)

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id,self.order.tracking_no)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pincode=models.CharField(max_length=150,null=False)

    def __str__(self):
        return self.user.username