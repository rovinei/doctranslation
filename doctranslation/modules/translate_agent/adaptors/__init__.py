from .base import TranslationAbtractAdaptor, OcrAbstractAdaptor
from .ocr.google_vision_adaptor import GoogleCloudVisionOCRAdaptor
from .translations.amazon_translation_adaptor import AmazonTranslateAdapter
from .translations.deepl_translation_adaptor import DeepLTranslationAdaptor
from .translations.google_translation_adaptor import GoogleTranslateAdapter
from .translations.microsoft_translation_adaptor import MicrosoftTranslateAdapter


__all__ = (
    'TranslationAbtractAdaptor',
    'OcrAbstractAdaptor',
    'DeepLTranslationAdaptor',
    'AmazonTranslateAdapter',
    'GoogleTranslateAdapter',
    'GoogleCloudVisionOCRAdaptor',
    'MicrosoftTranslateAdapter',
)
