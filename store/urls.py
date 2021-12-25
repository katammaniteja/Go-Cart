from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsView,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:pro_slug>',views.productView,name="productView"),
]