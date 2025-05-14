from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('auth/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('adduser/',views.AddUser,name="add_user"),
    

]