from .models import User

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def validate_username(self, value):
        """
        Validate the username field to ensure it only contains lowercase letters, numbers, and hyphens,
        and it must be unique.
        """
        if not value.islower():
            raise serializers.ValidationError('Username must be in lowercase.')
        if not value.isalnum() or "_" in value:
            raise serializers.ValidationError(
                'Username must only contain lowercase letters, numbers, and underscores.'
            )
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username is already taken.')
        return value

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            permission='user',
            is_active=True,
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name", "last_name")

        
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
