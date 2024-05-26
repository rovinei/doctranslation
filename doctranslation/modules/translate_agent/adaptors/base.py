from abc import ABC, abstractmethod


class TranslationAbtractAdaptor(ABC):
    @abstractmethod
    def translate_text(self, text, target_language, source_language, *args, **kwargs):
        pass
    
    @abstractmethod
    def translate_document(self, file_path, target_language, source_language, *args, **kwargs):
        pass

    @abstractmethod
    def detect_language(self, text, *args, **kwargs):
        pass


class OcrAbstractAdaptor(ABC):
    @abstractmethod
    def perform_ocr(self, image_path):
        pass
