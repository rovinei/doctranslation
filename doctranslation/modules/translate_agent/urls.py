from django.urls import path

from .views import FileDownloadView, PptxTranslationAPIView

app_name = 'Translate Agent'


urlpatterns = [
    path('download/<str:hex_id>', FileDownloadView.as_view({'get': 'retrieve'}), name='download-document'),
    path('', PptxTranslationAPIView.as_view(), name='pptx_translation'),
]
