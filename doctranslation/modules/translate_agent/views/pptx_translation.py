import os
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from doctranslation.modules.translate_agent.factories import TranslationServiceFactory
from doctranslation.modules.translate_agent.serializers import DocumentSerializer
from doctranslation.modules.translate_agent.models import Document
from doctranslation.modules.authentication.views.base import APICreateView

from ..serializers import PptxUploadSerializer


class PptxTranslationAPIView(APICreateView):
    def create(self, request, *args, **kwargs):
        serializer = PptxUploadSerializer(data=request.data)
        if serializer.is_valid():
            # Extract validated data
            pptx_file = serializer.validated_data['file']
            engine = serializer.validated_data['engine']
            is_translate_image = serializer.validated_data['is_translate_image']
            target_language = serializer.validated_data['target_language']
            source_language = serializer.validated_data['source_language']

            upload_dir = os.path.join(settings.BASE_DIR, 'uploads')

            # Ensure the upload directory exists
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            # Define the file path
            file_path = os.path.join(upload_dir, pptx_file.name)

            # Save the file to the defined path
            with open(file_path, 'wb') as f:
                for chunk in pptx_file.chunks():
                    f.write(chunk)

            translator = TranslationServiceFactory.get_translation_service(engine)
            translated_doc_path = translator.translate_document(
                file_path=file_path,
                target_language=target_language, 
                source_language=source_language,
            )

            # Save the document to the database
            filename = os.path.basename(translated_doc_path)
            document = Document.objects.create_document(
                name=filename,
                location=translated_doc_path,
            )
            document_serializer = DocumentSerializer(document)

            return Response({
                "message": "Successfully translated document",
                "document": document_serializer.data,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
