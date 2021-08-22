from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.UUIDField(source='id')

    class Meta:
        model = User
        exclude = ('id',)
