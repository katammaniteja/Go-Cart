from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Categories,Products
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'store/index.html');

def collections(request):
    category=Categories.objects.filter(status=0).order_by('-created_at')
    context={'category':category}
    return render(request, 'store/collections.html',context)

def collectionsView(request,slug):
    if Categories.objects.filter(slug=slug,status=0):
        products=Products.objects.filter(category__slug=slug).order_by('-created_at')
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

def TotalListAjax(request):
    products=Products.objects.filter(status=0).values_list('name',flat=True)
    categories=Categories.objects.filter(status=0).values_list('name',flat=True)
    products_list=list(products)
    categories_list=list(categories)
    return JsonResponse(products_list+categories_list,safe=False)

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