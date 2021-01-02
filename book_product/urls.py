from django.urls import path

from . import views

urlpatterns=[
    path('',views.product_added,name='product_added'),
    path('index',views.product_index,name='product_index'),
]
