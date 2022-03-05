from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from store.models import Products,Cart

def addtocart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Products.objects.filter(id=prod_id).first()
            if(product_check):
                if(Cart.objects.filter(user_id=request.user.id,product_id=prod_id).exists()):
                    return JsonResponse({'status':"Product already in the cart",'tag':"notify"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"Product added to cart",'tag':'success'})
                    else:
                        return JsonResponse({'status':"Only "+str(product_check.quantity)+" quantity available",'tag':'notify'})
            else:
                return JsonResponse({'status':"No such product found",'tag':'error'})
        else:
            return JsonResponse({'status':"Login to continue",'tag':'warning'})
    return redirect('/')

def viewcart(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        context={'cart':cart}
        return render(request,"cart.html",context)
    else:
        messages.error(request,"Please login to view your cart")
        return HttpResponseRedirect(reverse('loginpage'))

def updatecart(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id).exists()):
            prod_qty=int(request.POST.get('product_qty'))
            cart=Cart.objects.get(product_id=prod_id,user=request.user)
            cart.product_qty=prod_qty
            cart.save()
            return JsonResponse({'status':"Product Updated Successfully",'tag':'success'})
    return redirect('/')

def deletecartitem(request):
    if request.method=='POST':
        prod_id=int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id).exists()):
            cartitem=Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({'status':"Product removed from cart",'tag':'success'})
    return redirect("/")