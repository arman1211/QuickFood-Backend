from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsUser
from .models import Order
from .serializers import OrderSerializer, OrderByUserSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class UserOrdersAPIView(generics.ListAPIView):
    serializer_class = OrderByUserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id)

    def list(self, request, *args, **kwargs):
        """
        Override the list method to return all orders for the given user_id
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
