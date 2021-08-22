from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    _id = serializers.UUIDField(source='id')
    class Meta:
        model = Order
        exclude = ('id',)
