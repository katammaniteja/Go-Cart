from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from store.models import Order,OrderItem

def index(request):
    if not request.user.is_authenticated:
        messages.error(request,"Please login to continue")
        return HttpResponseRedirect(reverse('home'))
    orders=Order.objects.filter(user=request.user)
    context={"orders":orders}
    return render(request,'store/orders/index.html',context)

def vieworder(request,t_no):
    if not request.user.is_authenticated:
        messages.error(request,"Please login to continue")
        return HttpResponseRedirect(reverse('home'))
    order=Order.objects.get(tracking_no=t_no,user=request.user)
    orderItems=OrderItem.objects.filter(order=order)
    context={
        'order':order,
        "orderitems":orderItems
    }
    return render(request, 'store/orders/view.html',context) 