from doctranslation.modules.translate_agent.adaptors import TranslationAbtractAdaptor
from doctranslation.modules.translate_agent.services import MicrosoftTranslateService


class MicrosoftTranslateAdapter(TranslationAbtractAdaptor):
    def __init__(self, endpoint, subscription_key):
        self.service = MicrosoftTranslateService(endpoint, subscription_key)

    def translate_text(self, text, target_language, source_language):
        return self.service.translate_text(text, target_language, source_language)
    
    def translate_document(self, file_path, target_language, source_language):
        raise NotImplemented

    def detect_language(self, text):
        return self.service.detect_language(text)
