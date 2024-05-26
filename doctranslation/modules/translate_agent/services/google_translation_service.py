import mimetypes
import os

from django.conf import settings
from google.cloud import translate_v3beta1 as translate_v3
from google.oauth2 import service_account

from doctranslation.modules.translate_agent.constants import GOOGLE_ALLOW_TRANSLATE_DOC_MIME_TYPES

from .mixin import TranslationServiceMixin


class GoogleTranslateService(TranslationServiceMixin):
    def __init__(self, service_account_key_file):
        # Initialize the translation client
        credentials = service_account.Credentials.from_service_account_file(service_account_key_file)
        self.client = translate_v3.TranslationServiceClient(credentials=credentials)

    def translate_text(self, text, target_language, source_language=None):
        if not source_language:
            source_language = self.auto_detect_language(text)

        if type(text) is not list:
            text = [text]
        request = {
            "parent": f"projects/{settings.GOOGLE_PROJECT_ID}/locations/{settings.GOOGLE_REGION}",
            "contents": text,
            "target_language_code": target_language,
            "source_language_code": source_language,
        }

        result = self.client.translate_text(request=request)

        return result.translations

    def translate_document(self, file_path, target_language, source_language):
        # Validate file type
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type not in GOOGLE_ALLOW_TRANSLATE_DOC_MIME_TYPES:
            raise ValueError(f"Not supported translation file type: {mime_type}")

        # Read the document content
        with open(file_path, "rb") as document:
            document_content = document.read()

        # Specify the document input configuration
        document_input_config = {
            "content": document_content,
            "mime_type": mime_type,
        }

        # Specify the translation request
        request = {
            "parent": f"projects/{settings.GOOGLE_PROJECT_ID}/locations/{settings.GOOGLE_REGION}",
            "document_input_config": document_input_config,
            "target_language_code": target_language,
            "source_language_code": source_language,
        }

        # Perform the document translation
        response = self.client.translate_document(request=request)

        # Write the translated document to a file
        translated_file_path = os.path.join(os.path.dirname(file_path), f"translated_{os.path.basename(file_path)}")
        with open(translated_file_path, "wb") as translated_document:
            translated_document.write(response.document_translation.byte_stream_outputs[0])

        return translated_file_path

    def detect_language(self, text):
        result = self.client.detect_language(text)
        return result['language']
