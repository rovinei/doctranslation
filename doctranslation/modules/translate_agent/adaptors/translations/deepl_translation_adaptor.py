from doctranslation.modules.translate_agent.adaptors import TranslationAbtractAdaptor
from doctranslation.modules.translate_agent.services import DeepLTranslateService

class DeepLTranslationAdaptor(TranslationAbtractAdaptor):
    def __init__(self, auth_key):
        self.service = DeepLTranslateService(auth_key)

    def translate_text(self, text, target_language):
        return self.service.translate_text(text, target_language)

    def detect_language(self, text):
        return self.service.detect_language(text)