from django.conf import settings

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
            return GoogleTranslateAdapter(service_account_key_file=settings.GOOGLE_APPLICATION_CREDENTIALS_PATH, **kwargs)
        elif service_name == "microsoft":
            return MicrosoftTranslateAdapter(endpoint=None, subscription_key=None, **kwargs)
        elif service_name == "amazon":
            return AmazonTranslateAdapter(aws_access_key_id=None, aws_secret_access_key=None, **kwargs)
        elif service_name == "deepl":
            return DeepLTranslationAdaptor(auth_key=None, **kwargs)
        else:
            raise ValueError(f"Unknown service: {service_name}")
