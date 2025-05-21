from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'order-items', views.OrderItemViewSet)
router.register(r'order-updates', views.OrderUpdateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order-status/<int:order_id>/', views.get_order_status, name='get_order_status'),
    path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
]