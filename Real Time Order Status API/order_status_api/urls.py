from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.home, name='home'),  # Add homepage view
]

if __name__ == "__main__":
    import os
    os.system("flask run")
