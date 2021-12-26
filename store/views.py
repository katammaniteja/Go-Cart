from django.shortcuts import render,HttpResponseRedirect
from .models import Categories,Products
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'store/index.html');

def collections(request):
    category=Categories.objects.filter(status=0)
    context={'category':category}
    return render(request, 'store/collections.html',context)

def collectionsView(request,slug):
    if Categories.objects.filter(slug=slug,status=0):
        products=Products.objects.filter(category__slug=slug)
        category=Categories.objects.filter(slug=slug).first()
        context={"products":products,"category":category};
        return render(request, 'store/products/index.html',context)
    else:
        messages.error(request,"No such category found");
        return HttpResponseRedirect(reverse('home'))

def productView(request,cate_slug,pro_slug):
    if Categories.objects.filter(slug=cate_slug,status=0):
        if Products.objects.filter(slug=pro_slug,status=0):
            products=Products.objects.filter(slug=pro_slug,status=0).first()
            context={"products":products}
            return render(request, 'store/products/view.html',context)
        else:
            messages.error(request,"No such product found");
            return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request,"No such category found");
        return HttpResponseRedirect(reverse('home'))
