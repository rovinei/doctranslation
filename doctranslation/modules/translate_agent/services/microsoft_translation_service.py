from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text import TextTranslationClient

from .mixin import TranslationServiceMixin


class MicrosoftTranslateService(TranslationServiceMixin):
    def __init__(self, endpoint, subscription_key):
        self.client = TextTranslationClient(endpoint, AzureKeyCredential(subscription_key))

    def translate_text(self, text, target_language=None):
        if not target_language:
            target_language = self.auto_detect_language(text)

        response = self.client.translate(content=[text], to=[target_language])
        translated_text = response[0].translations[0].text
        return translated_text

    def detect_language(self, text):
        response = self.client.detect_language(content=[text])
        detected_language = response[0].primary_language.language
        return detected_language
