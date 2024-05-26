from google.cloud import translate_v2 as translate

from .mixin import TranslationServiceMixin


class GoogleTranslateService(TranslationServiceMixin):
    def __init__(self, service_account_file):
        self.client = translate.Client.from_service_account_json(service_account_file)

    def translate_text(self, text, target_language=None):
        if not target_language:
            target_language = self.auto_detect_language(text)

        result = self.client.translate(text, target_language=target_language)
        return result['translatedText']

    def detect_language(self, text):
        result = self.client.detect_language(text)
        return result['language']
