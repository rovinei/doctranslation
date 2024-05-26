from doctranslation.modules.translate_agent.adaptors import TranslationAbtractAdaptor
from doctranslation.modules.translate_agent.services import AmazonTranslateService

class AmazonTranslateAdapter(TranslationAbtractAdaptor):
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        self.service = AmazonTranslateService(aws_access_key_id, aws_secret_access_key, region_name)

    def translate_text(self, text, target_language):
        return self.service.translate_text(text, target_language)

    def detect_language(self, text):
        return self.service.detect_language(text)