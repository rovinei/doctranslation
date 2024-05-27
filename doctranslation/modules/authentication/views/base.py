import logging

from django.core.exceptions import PermissionDenied
from django.http import Http404
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView, exception_handler
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet

from doctranslation.modules.authentication.authentication import APITokenAuthentication
from doctranslation.modules.authentication.exceptions import (
    AuthFailedException,
    MethodNotAllowedException,
    NotFoundException,
    OperationNotAllowedException,
    ServerErrorException,
    WrongParameterException,
)

logger = logging.getLogger(__name__)


def api_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = NotFoundException()
    elif isinstance(exc, AuthenticationFailed):
        exc = AuthFailedException()
    elif isinstance(exc, PermissionDenied):
        exc = OperationNotAllowedException()
    elif isinstance(exc, ValidationError):
        logger.warning(exc)
        exc = WrongParameterException(exc.detail)

    response = exception_handler(exc, context)
    if not response:
        logger.exception(exc)
        return Response(ServerErrorException.to_dict(), status=ServerErrorException.status_code)
    return response


class APILimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 1000


class APIViewMixin:
    authentication_classes = (APITokenAuthentication,)
    pagination_class = APILimitOffsetPagination
    renderer_classes = (CamelCaseJSONRenderer, BrowsableAPIRenderer)

    def get_exception_handler(self):
        return api_exception_handler

    def http_method_not_allowed(self, request, *args, **kwargs):
        raise MethodNotAllowedException


class APIBaseView(APIViewMixin, APIView):
    pass


class APIListView(APIViewMixin, ListAPIView):
    pass


class APICreateView(APIViewMixin, CreateAPIView):
    pass


class APIModelViewSet(APIViewMixin, ModelViewSet):
    pass


class APIReadOnlyViewSet(APIViewMixin, ReadOnlyModelViewSet):
    pass


class APIRetrieveOnlyViewSet(APIViewMixin, RetrieveModelMixin, GenericViewSet):
    pass


class APICreateOnlyViewSet(APIViewMixin, CreateModelMixin, GenericViewSet):
    pass


class APIRetrieveUpdateViewSet(APIViewMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    pass


class APIListViewSet(APIViewMixin, ListModelMixin, GenericViewSet):
    pass


class APIListCreateViewSet(APIViewMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    pass


class APICreateDestroyViewSet(APIViewMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    pass
