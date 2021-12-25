from django.shortcuts import render,HttpResponseRedirect
from .models import Categories,Products
from django.urls import reverse

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
    return HttpResponseRedirect(reverse('home'))