from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def Register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            form.save();
            messages.success(request,"Registered Successfully! Login to continue")
            send_mail(
                subject="Welcome to Go Cart", 
                message="You have successfully registered to Go Cart. Thank you for being a part", 
                from_email="Go Cart",
                auth_user=settings.EMAIL_HOST_USER, 
                recipient_list=[request.POST.get('email')],
                fail_silently=False
            )
            return redirect('/login')
    context={"form":form}
    return render(request, "auth/register.html",context)

def Login(request):
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
        return render(request,'auth/login.html')

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out successfully")
    else:
        messages.error(request,"Invalid operation")
    return redirect('/')
