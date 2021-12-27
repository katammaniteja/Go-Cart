from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from store.forms import customForm
from django.contrib import messages
def register(request):
    form=customForm()
    if request.method=='POST':
        form=customForm(request.POST)
        if form.is_valid():
            form.save();
            messages.success(request,"Registered Successfully! Login to continue")
            return redirect('/login')
    context={"form":form}
    return render(request, "store/auth/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=name,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect('/login')
        return render(request,'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    return redirect('/')
