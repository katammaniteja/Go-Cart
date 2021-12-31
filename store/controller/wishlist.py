from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from store.models import Wishlist,Products

from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    wishlist=Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request, 'store\wishlist.html',context)

def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Products.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                    return JsonResponse({"status":"product already in the wishlist","tag":"success"})
                else:
                    Wishlist.objects.create(user=request.user,product_id=prod_id)
                    return JsonResponse({'status':'product added to the wishlist','tag':'success'})
            else:
                return JsonResponse({"status":"No such product found",'tag':'error'})

        else:
            return JsonResponse({'status':"login to continue",'tag':'warning'})
    return redirect('/')

def deletewishitem(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
                wishlistitem=Wishlist.objects.filter(user=request.user,product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({"status":"product removed from wishlist","tag":"success"})
            else:
                return JsonResponse({'status':'product not found in wishlist','tag':'error'})
        else:
            return JsonResponse({'status':"login to continue",'tag':'warning'})
    return redirect('/')