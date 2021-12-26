from django.db import models
import datetime
import os

from django.contrib.auth.models import User

# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowtime=datetime.datetime.now().strftime('%Y%m%H:%M:%S')
    filename="%s%s" % (nowtime,original_filename)
    return os.path.join('uploads/',filename)

class Categories(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,blank=True,null=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    meta_title=models.CharField(max_length=150,null=True,blank=True)
    meta_keywords=models.CharField(max_length=150,null=True,blank=True)
    meta_description=models.CharField(max_length=150,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,blank=True,null=True)
    small_description=models.TextField(max_length=700,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag=models.CharField(max_length=150,null=True,blank=True)
    meta_title=models.CharField(max_length=150,null=True,blank=True)
    meta_keywords=models.CharField(max_length=150,null=True,blank=True)
    meta_description=models.CharField(max_length=150,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Products, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)