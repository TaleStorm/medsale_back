from rest_framework import serializers

from order.srializers import OrderSerializer
from product.srializers import ProductSerializer
from user.srializers import UserSerializer


class OrderResponseSerializer(serializers.Serializer):
    data = OrderSerializer()
    status = serializers.BooleanField()