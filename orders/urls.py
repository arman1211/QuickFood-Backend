from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, UserOrdersAPIView

# Create a router for order-related URLs
router = DefaultRouter()
router.register(r"", OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('user/<int:user_id>', UserOrdersAPIView.as_view()),  
]
