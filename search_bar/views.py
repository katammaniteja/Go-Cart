from store.models import Products,Categories
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib import messages
from rest_framework import status

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