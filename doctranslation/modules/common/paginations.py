from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework_extensions.mixins import PaginateByMaxMixin


class StandardResultsSetPagination(PaginateByMaxMixin, PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 200

    def paginate_queryset(self, queryset, request, view=None):
        """
        Return queryset.all() when page_size is -1.
        """
        if request.query_params.get(self.page_size_query_param) == '-1':
            page_size = queryset.count()
            if not page_size:
                return super().paginate_queryset(queryset, request, view=None)

            paginator = self.django_paginator_class(queryset, page_size)
            page_number = paginator.num_pages

            try:
                self.page = paginator.page(page_number)
            except InvalidPage as exc:
                msg = self.invalid_page_message.format(
                    page_number=page_number, message=str(exc),
                )
                raise NotFound(msg)

            self.request = request
            return list(self.page)
        else:
            return super().paginate_queryset(queryset, request, view=None)
