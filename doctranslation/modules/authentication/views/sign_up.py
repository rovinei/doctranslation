from django.contrib.auth import login
from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from doctranslation.modules.authentication.serializers import SignUpSerializer, UserSerializer


class SignUpView(APIView):
    permission_classes = (AllowAny,)

    @transaction.atomic
    def post(self, request):
        signup = SignUpSerializer(data=request.data)
        signup.is_valid(raise_exception=True)
        user = signup.save()
        if user.is_active:
            login(request, user)

        return Response(UserSerializer(user).data)
