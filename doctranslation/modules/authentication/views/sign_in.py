from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from doctranslation.modules.authentication.serializers import UserSerializer, UserSignedInSerializer

class SignInSerializer(serializers.Serializer):
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


class SignInView(APIView):
    permission_classes = (AllowAny,)

    @transaction.atomic
    def post(self, request):
        signin = SignInSerializer(data=request.data)

        signin.is_valid(raise_exception=True)
        user = signin.save()
        login(request, user)
        return Response(UserSignedInSerializer(user).data)


class SignOutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response({})
