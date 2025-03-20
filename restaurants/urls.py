from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, MenuItemViewSet

# Create a router for restaurant-related URLs
router = DefaultRouter()
router.register(r"", RestaurantViewSet)


urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
