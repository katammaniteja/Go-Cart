from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib import messages
from store.models import Products,Cart

def index(request):
    rawcart=Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty>item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems=Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price+=item.product.selling_price*item.product_qty

    context={'cartitems':cartitems,'total_price':total_price}
    return render(request,'store/checkout.html',context)