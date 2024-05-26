import requests

from .mixin import TranslationServiceMixin


class DeepLTranslateService(TranslationServiceMixin):
    def __init__(self, auth_key):
        self.auth_key = auth_key

    def translate_text(self, text, target_language=None):
        if not target_language:
            target_language = self.auto_detect_language(text)

        url = "https://api.deepl.com/v2/translate"
        params = {
            "auth_key": self.auth_key,
            "text": text,
            "target_lang": target_language
        }
        response = requests.post(url, data=params)
        translation = response.json()["translations"][0]["text"]
        return translation

    def detect_language(self, text):
        url = "https://api.deepl.com/v2/language-detection"
        params = {
            "auth_key": self.auth_key,
            "text": text
        }
        response = requests.post(url, data=params)
        detected_language = response.json()["detected_languages"][0]["language"]
        return detected_language