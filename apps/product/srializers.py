from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    _id = serializers.UUIDField(source='id')

    class Meta:
        model = Product
        exclude = ('id',)
