from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from doctranslation.modules.authentication.validators import UserNameValidator
from doctranslation.modules.common.serializers import CustomErrorMessagesMixin


class SignUpSerializer(CustomErrorMessagesMixin, serializers.Serializer):
    email = serializers.EmailField(
        max_length=200, validators=[UniqueValidator(queryset=get_user_model().objects.filter())],
    )
    username = serializers.CharField(
        max_length=128,
        validators=[
            UniqueValidator(queryset=get_user_model().objects.filter()),
            UserNameValidator(),
        ],
    )
    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        extra_kwargs = {'password': {'write_only': True}}

    def __init__(self, data):
        super().__init__(data=data)

    def validate_confirm_password(self, value):
        password = self.initial_data.get('password', None)

        if (value and value == password) or not password:
            return value

        else:
            raise serializers.ValidationError('mismatch')

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        username = validated_data.get('username')
        return get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username,
        )
