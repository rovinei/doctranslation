import logging

from doctranslation.modules.common.utils.text_util import detect_language as detect_language_util

logger = logging.getLogger(__name__)


class TranslationServiceMixin:
    def auto_detect_language(self, text):
        try:
            target_language = self.detect_language(text)
        except Exception as e:
            logger.warning(f"Failed to detect language: {e}")
            target_language = detect_language_util(text)

        return target_language
