from django.db import models
import datetime
import os

# Create your models here.
def get_file_path(request,filename):
    original_filename=filename
    nowtime=datetime.datetime.now().strftime('%Y%m%H:%M:%S')
    filename="%s%s" % (nowtime,original_filename)
    return os.path.join('uploads/',filename)

class Categories(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    snall_description=models.TextField(max_length=500,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag=models.CharField(max_length=150,null=True,blank=True)
    meta_title=models.CharField(max_length=150,null=False,blank=False)
    meta_keywords=models.CharField(max_length=150,null=False,blank=False)
    meta_description=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name