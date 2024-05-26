from abc import ABC, abstractmethod


class TranslationAbtractAdaptor(ABC):
    @abstractmethod
    def translate_text(self, text, target_language, *args, **kwargs):
        pass

    @abstractmethod
    def detect_language(self, text, *args, **kwargs):
        pass
