from django.contrib.auth import get_user_model
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.viewsets import GenericViewSet

from doctranslation.modules.common.views.mixin import BaseModelViewSet

from ..serializers import UserSerializer


class UserView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CamelCaseJSONRenderer, BrowsableAPIRenderer)
    serializer_class = UserSerializer

    def get_exception_handler(self):
        return exception_handler

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(data=serializer.data)


class UserViewSet(
    BaseModelViewSet,
):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CamelCaseJSONRenderer, BrowsableAPIRenderer)
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_user_model().objects.filter(is_active=True, is_superuser=False)
