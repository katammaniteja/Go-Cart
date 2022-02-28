from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Categories,Products
from django.urls import reverse
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

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

class TotalListAjax(APIView):
    def get(self,request):
        products=Products.objects.filter(status=0).values_list('name',flat=True)
        categories=Categories.objects.filter(status=0).values_list('name',flat=True)
        products_list=list(products)
        categories_list=list(categories)
        return Response(products_list+categories_list,status=status.HTTP_200_OK)

def searched(request):
    if request.method=='POST':
        searched_item=request.POST.get('searched_item')
        if searched_item=="":
            return redirect(request.META.get("HTTP_REFERER"))
        product=Products.objects.filter(name=searched_item).first()
        category=Categories.objects.filter(name=searched_item).first()
        if product:
            return redirect('collections/'+product.category.slug+'/'+product.slug)
        elif category:
            return redirect('collections/'+category.slug)
        else:
            messages.error(request,"No such product found")
            return redirect(request.META.get("HTTP_REFERER"))
    return redirect(request.META.get("HTTP_REFERER"))