from doctranslation.modules.translate_agent.adaptors import GoogleCloudVisionOCRAdaptor

class OcrServiceFactory:

    @staticmethod
    def get_ocr_service(service_name, **kwargs):
        if service_name == 'google':
            return GoogleCloudVisionOCRAdaptor(**kwargs)
        else:
            raise ValueError(f"Unsupported OCR service type: {service_name}")
