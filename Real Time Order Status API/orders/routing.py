from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/orders/(?P<order_id>\w+)/$', consumers.OrderStatusConsumer.as_asgi),
]



## Additional Notes

1. I also noticed a potential issue in your `orders/routing.py` file. The WebSocket consumer connection method should be `as_asgi()` instead of `as_connect`:
```python
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/orders/(?P<order_id>\w+)/$', consumers.OrderStatusConsumer.as_asgi),
]