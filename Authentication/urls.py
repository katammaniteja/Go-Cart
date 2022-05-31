from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='loginpage'),
    path('logout/',views.Logout,name='logoutpage'),
]