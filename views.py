from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Customer, Order, Product, OrderItem, OrderUpdate
from .serializers import (
    CustomerSerializer, OrderSerializer, ProductSerializer,
    OrderItemSerializer, OrderUpdateSerializer
)
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        """
        This view should return a list of all orders
        for the currently authenticated user.
        """
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        
        customer = Customer.objects.filter(user=user).first()
        if customer:
            return Order.objects.filter(customer=customer)
        return Order.objects.none()

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderUpdateViewSet(viewsets.ModelViewSet):
    queryset = OrderUpdate.objects.all()
    serializer_class = OrderUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Update the order status
        order_update = serializer.instance
        order = order_update.order
        order.status = order_update.status
        order.save()
        
        # Send real-time update via WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"order_{order.id}",
            {
                "type": "order_status_update",
                "message": OrderUpdateSerializer(order_update).data
            }
        )
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_order_status(request, order_id):
    """
    Get the current status of an order
    """
    try:
        order = Order.objects.get(id=order_id)
        
        # Check if the user has permission to view this order
        user = request.user
        if not user.is_staff and order.customer.user != user:
            return Response({"detail": "You do not have permission to view this order."}, 
                            status=status.HTTP_403_FORBIDDEN)
        
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def update_order_status(request, order_id):
    """
    Update the status of an order and create an OrderUpdate entry
    """
    try:
        order = Order.objects.get(id=order_id)
        
        # Only staff can update order status
        if not request.user.is_staff:
            return Response({"detail": "You do not have permission to update order status."}, 
                            status=status.HTTP_403_FORBIDDEN)
        
        new_status = request.data.get('status')
        if not new_status:
            return Response({"detail": "Status is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create order update
        order_update = OrderUpdate.objects.create(
            order=order,
            status=new_status,
            location=request.data.get('location'),
            notes=request.data.get('notes')
        )
        
        # Update order status
        order.status = new_status
        order.save()
        
        # Send real-time update via WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"order_{order.id}",
            {
                "type": "order_status_update",
                "message": OrderUpdateSerializer(order_update).data
            }
        )
        
        return Response(OrderUpdateSerializer(order_update).data)
    except Order.DoesNotExist:
        return Response({"detail": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
