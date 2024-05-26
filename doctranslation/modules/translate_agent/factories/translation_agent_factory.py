from doctranslation.modules.translate_agent.adaptors import (
    AmazonTranslateAdapter,
    DeepLTranslationAdaptor,
    GoogleTranslateAdapter,
    MicrosoftTranslateAdapter,
)


class TranslationServiceFactory:
    @staticmethod
    def get_translation_service(service_name, **kwargs):
        if service_name == "google":
            return GoogleTranslateAdapter(**kwargs)
        elif service_name == "microsoft":
            return MicrosoftTranslateAdapter(**kwargs)
        elif service_name == "amazon":
            return AmazonTranslateAdapter(**kwargs)
        elif service_name == "deepl":
            return DeepLTranslationAdaptor(**kwargs)
        else:
            raise ValueError(f"Unknown service: {service_name}")
