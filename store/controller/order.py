from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from store.models import Order,OrderItem
from django.contrib.auth.decorators import login_required

def index(request):
    orders=Order.objects.filter(user=request.user)
    context={"orders":orders}
    return render(request,'store/orders/index.html',context)

def vieworder(request,t_no):
    order=Order.objects.filter(tracking_no=t_no).filter(user=request.user).first()
    orderItems=OrderItem.objects.filter(order=order)
    context={
        'order':order,
        "orderitems":orderItems
    }
    return render(request, 'store/orders/view.html',context) 