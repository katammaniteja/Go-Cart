from django.urls import path
from . import views
from store.controller import cart,wishlist,checkout,order

urlpatterns=[
    path('',views.home,name='home'),
    path('collections/',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsView,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:pro_slug>',views.productView,name="productView"),

    path('add-to-cart',cart.addtocart,name='addtocart'),
    path('cart',cart.viewcart,name='viewcart'),
    path('update-cart',cart.updatecart,name='updatecart'),
    path('delete-cart-item',cart.deletecartitem,name='deletecartitem'),

    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist',wishlist.addtowishlist,name="addtowishlist"),
    path('delete-wishlist-item',wishlist.deletewishitem,name="deletewishlistitem"),

    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),

    path('proceed-to-pay',checkout.razorpaycheck),
    path('my-orders',order.index,name="myorders"),
    path('view-order/<str:t_no>',order.vieworder,name="orderview")
]