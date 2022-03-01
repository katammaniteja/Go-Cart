from django.urls import path
from . import views

urlpatterns=[
    path('items_list',views.TotalListAjax.as_view()),
    path('searched',views.searched,name="searched"),
]