from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsRestaurantOwner
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
