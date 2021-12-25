from django.shortcuts import render
from .models import Categories,Products

# Create your views here.
def home(request):
    return render(request,'store/index.html');

def collections(request):
    category=Categories.objects.filter(status=0)
    context={'category':category}
    return render(request, 'store/collections.html',context)