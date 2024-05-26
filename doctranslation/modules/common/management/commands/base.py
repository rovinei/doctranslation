import logging
from abc import ABCMeta, abstractmethod

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class CommonBaseCommand(BaseCommand, metaclass=ABCMeta):

    def __init__(self):
        super().__init__()
        self.options = None

    @abstractmethod
    def get_process_name(self):
        pass

    @abstractmethod
    def do_handle(self, *args, **options):
        pass

    def handle(self, *args, **options):
        self.options = options
        name = self.get_process_name()
        try:
            logger.info('%s is starting', name)
            self.do_handle(*args, **options)
        except Exception as e:
            logger.exception(e)
            raise
