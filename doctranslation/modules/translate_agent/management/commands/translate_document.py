import os
import logging

from django.conf import settings

from doctranslation.modules.common.management.commands.base import CommonBaseCommand
from doctranslation.modules.translate_agent.factories import TranslationServiceFactory

logger = logging.getLogger(__name__)

PER_PAGE = 10_000


class Command(CommonBaseCommand):
    help = 'Translate document'

    def get_process_name(self):
        return os.path.splitext(os.path.basename(__file__))[0]
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--document-path', type=str, nargs='?', required=True,
        )
        parser.add_argument(
            '--target-language', type=str, nargs='?', required=True,
        )
        parser.add_argument(
            '--source-language', type=str, nargs='?', required=True,
        )

    def do_handle(self, *args, **options):
        translator = TranslationServiceFactory.get_translation_service(
            "google",
            service_account_key_file=settings.GOOGLE_APPLICATION_CREDENTIALS_PATH,
        )
        translated_document_path = translator.translate_document(
            file_path=options['document_path'],
            target_language=options['target_language'],
            source_language=options['source_language'],
        )
        message = f'Translated document is saved at {translated_document_path}'
        logger.info(message)
        print(message)
