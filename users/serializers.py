from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User
    """
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "phone_number", "country", "avatar"]
