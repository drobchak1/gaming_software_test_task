import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from pro_gaming import routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pro_gaming.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Handles HTTP connections
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Handles WebSocket connections
        )
    ),
})
