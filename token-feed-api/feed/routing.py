from django.urls import re_path
from .consumers import TokenFeedConsumer

websocket_urlpatterns = [
    re_path(r'ws/feed/$', TokenFeedConsumer.as_asgi()),
]
