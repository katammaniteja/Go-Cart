from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Categories,Products
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    trending_products=Products.objects.filter(trending=1)
    category=Categories.objects.filter(status=0)
    context={'trending_products':trending_products,'category':category}
    return render(request,'index.html',context);

def collections(request):
    category=Categories.objects.filter(status=0)
    context={'category':category}
    return render(request, 'collections.html',context)

def collectionsView(request,slug):
    if Categories.objects.filter(slug=slug,status=0).exists():
        products=Products.objects.filter(category__slug=slug)
        category=Categories.objects.get(slug=slug)
        context={"products":products,"category":category};
        return render(request, 'products/index.html',context)
    else:
        messages.error(request,"No such category found");
        return HttpResponseRedirect(reverse('home'))

def productView(request,cate_slug,pro_slug):
    if Categories.objects.filter(slug=cate_slug,status=0).exists():
        if Products.objects.filter(slug=pro_slug,status=0).exists():
            products=Products.objects.get(slug=pro_slug,status=0)
            context={"products":products}
            return render(request, 'products/view.html',context)
        else:
            messages.error(request,"No such product found");
            return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request,"No such category found");
        return HttpResponseRedirect(reverse('home'))
