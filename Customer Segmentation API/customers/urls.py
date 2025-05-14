from django.contrib import admin
from django.urls import path,include
from .views import SegmentedCustomers,Customers

urlpatterns = [
    path('home',SegmentedCustomers),
    path('customers',Customers),
]