from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.mixins import DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.views import exception_handler
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet

from doctranslation.modules.common.paginations import StandardResultsSetPagination


class BaseAPIViewMixin:
    renderer_classes = (
        CamelCaseJSONRenderer,
        BrowsableAPIRenderer,
    )

    def get_exception_handler(self):
        return exception_handler


class BaseViewSetMixin(BaseAPIViewMixin):
    pagination_class = StandardResultsSetPagination


class BaseModelViewSet(BaseViewSetMixin, ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'options']


class BaseReadOnlyModelViewSet(BaseViewSetMixin, ReadOnlyModelViewSet):
    pass


class BaseListModelViewSet(BaseViewSetMixin, ListModelMixin, GenericViewSet):
    pass


class BaseRetrieveModelViewSet(BaseViewSetMixin, RetrieveModelMixin, GenericViewSet):
    pass


class BaseAPIView(BaseViewSetMixin, GenericAPIView):
    pass


class BaseListAPIView(BaseViewSetMixin, ListAPIView):
    pass


class BaseRetrieveAPIView(BaseViewSetMixin, RetrieveAPIView):
    pass


class BaseDestroyAPIView(BaseViewSetMixin, DestroyAPIView):
    pass


class BaseUpdateAPIView(BaseViewSetMixin, UpdateAPIView):
    pass


class BaseCreateAPIView(BaseViewSetMixin, CreateAPIView):
    pass


class BaseListCreateAPIView(BaseViewSetMixin, ListCreateAPIView):
    pass


class BaseRetrieveUpdateModelViewSet(BaseViewSetMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    pass


class BaseDestroyModelViewSet(BaseViewSetMixin, DestroyModelMixin, GenericViewSet):
    pass
