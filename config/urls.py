import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from doctranslation.urls import urlpatterns as old_urlpatterns


urlpatterns = old_urlpatterns

if settings.DEBUG or settings.TESTING:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT,
    ) + static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    ) + urlpatterns
