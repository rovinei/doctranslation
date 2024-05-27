import os
from django.conf import settings
from rest_framework import status
from django.http import Http404, FileResponse

from doctranslation.modules.authentication.views.base import APIRetrieveOnlyViewSet
from doctranslation.modules.translate_agent.models import Document


class FileDownloadView(APIRetrieveOnlyViewSet):
    def retrieve(self, request, *args, **kwargs):
        hex_id = kwargs.get('hex_id')
        if document := Document.objects.get_by_hex_id(hex_id):
            if file := document.get_file():
                return FileResponse(file, as_attachment=True, filename=document.name)

        raise Http404("File not found")