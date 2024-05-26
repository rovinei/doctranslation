from doctranslation.modules.translate_agent.adaptors import OcrAbstractAdaptor
from doctranslation.modules.translate_agent.services import GoogleCloudVisionOCRService


class GoogleCloudVisionOCRAdaptor(OcrAbstractAdaptor):

    def __init__(self, service_account_key_file):
        self.service = GoogleCloudVisionOCRService(service_account_key_file)

    def perform_ocr(self, image_path):
        return self.service.perform_ocr(image_path)
