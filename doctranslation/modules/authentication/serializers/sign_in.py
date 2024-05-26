from django.contrib.auth import authenticate
from rest_framework import serializers

from doctranslation.modules.common.serializers import CustomErrorMessagesMixin


class SignInSerializer(CustomErrorMessagesMixin, serializers.Serializer):
    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError({'email': ['wrongCredentials'], 'password': ['wrongCredentials']})

        if not user.is_active:
            raise serializers.ValidationError({'email': ['notActive']})

        return user
