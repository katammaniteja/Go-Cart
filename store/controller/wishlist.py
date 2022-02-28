from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from store.models import Wishlist,Products
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        wishlist=Wishlist.objects.filter(user=request.user)
        context={'wishlist':wishlist}
        return render(request, 'wishlist.html',context)
    else:
        messages.error(request,"Please login to view your wishlist")
        return HttpResponseRedirect(reverse('loginpage'))

def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Products.objects.filter(id=prod_id).exists()):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id).exists()):
                    return JsonResponse({"status":"Product already in the wishlist","tag":"notify"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'Product added to the wishlist','tag':'success'})
            else:
                return JsonResponse({"status":"No such product found",'tag':'error'})
        else:
            return JsonResponse({'status':"Login to continue",'tag':'warning'})
    return redirect('/')

def deletewishitem(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id).exists()):
                wishlistitem=Wishlist.objects.get(user=request.user,product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({"status":"Product removed from wishlist","tag":"success"})
            else:
                return JsonResponse({'status':'Product not found in wishlist','tag':'error'})
        else:
            return JsonResponse({'status':"login to continue",'tag':'warning'})
    return redirect('/')