from doctranslation.modules.translate_agent.adaptors import TranslationAbtractAdaptor
from doctranslation.modules.translate_agent.services import GoogleTranslateService


class GoogleTranslateAdapter(TranslationAbtractAdaptor):
    def __init__(self, service_account_key_file):
        self.service = GoogleTranslateService(service_account_key_file)

    def translate_text(self, text, target_language):
        return self.service.translate_text(text, target_language)
    
    def translate_document(self, file_path, target_language, source_language):
        return self.service.translate_document(file_path, target_language, source_language)

    def detect_language(self, text):
        return self.service.detect_language(text)
