from rest_framework import serializers
from .models import Order, DeliveryAddress,Cart, CartItem
from django.db import transaction
from restaurants.models import MenuItem

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    delivery_address = DeliverySerializer(read_only = True)
    ordered_items = serializers.SerializerMethodField(read_only=True)
    cart_items = serializers.DictField(write_only=True)  # Cart items from frontend (menu_id: quantity)
    user_details = serializers.DictField(write_only=True)  # User address details
    delivery_fee = serializers.DecimalField(max_digits=10, decimal_places=2, write_only=True)

    class Meta:
        model = Order
        fields = "__all__"
    
    def get_ordered_items(self,obj):
        return obj.get_ordered_items()

    def create(self, validated_data):
        user = self.context["request"].user
        cart_items_data = validated_data.pop("cart_items")  # Extract cart items
        user_details = validated_data.pop("user_details")  # Extract user details
        delivery_fee = validated_data.pop("delivery_fee")

        with transaction.atomic():
            # Step 1: Create Delivery Address
            delivery_address = DeliveryAddress.objects.create(
                user=user,
                first_name=user_details.get("firstName"),
                last_name=user_details.get("lastName"),
                email=user_details.get("email"),
                street=user_details.get("street"),
                city=user_details.get("city"),
                state=user_details.get("state"),
                zip_code=user_details.get("zipCode"),
                country=user_details.get("country"),
                phone=user_details.get("phone"),
            )

            # Step 2: Create a new Cart
            cart = Cart.objects.create(user=user)

            # Step 3: Create Cart Items & Calculate Total Price
            total_price = 0
            for menu_id, quantity in cart_items_data.items():
                try:
                    menu_item = MenuItem.objects.get(id=menu_id)
                except MenuItem.DoesNotExist:
                    raise serializers.ValidationError(f"Menu item with ID {menu_id} does not exist.")

                CartItem.objects.create(cart=cart, menu_item=menu_item, quantity=quantity)
                total_price += menu_item.price * quantity

            # Step 4: Add Delivery Fee
            total_price += delivery_fee

            # Step 5: Create Order
            order = Order.objects.create(
                user=user,
                cart=cart,
                delivery_address=delivery_address,
                total_price=total_price,
                status="preparing",
            )

        return order


class OrderByUserSerializer(serializers.ModelSerializer):
    item_details = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Order
        fields = "__all__"
    
    def get_item_details(self,obj):
        return obj.get_ordered_items()