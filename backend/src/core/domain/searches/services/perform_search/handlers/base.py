import abc
import logging
from pathlib import Path

from django.db import transaction

from core.infra.searches.models import SearchFilter


logger = logging.getLogger('services')


class BaseSearchFilterHandler(abc.ABC):
    """Абстрактный класс для проведения поиска по определенному фильтру."""

    @staticmethod
    def can_handle(search_filter: SearchFilter) -> bool:
        """Выполняет проверку корректности фильтра."""

        return False

    @abc.abstractmethod
    def handle(self, file_path: Path, search_filter: SearchFilter) -> bool:
        """Выполняет непосредственные действие фильтра."""

        raise NotImplementedError

    @transaction.atomic
    def execute(self, file_path: Path, search_filter: SearchFilter) -> bool:
        if not self.can_handle(search_filter):
            return True

        try:
            return self.handle(file_path, search_filter)
        except FileNotFoundError:
            logger.debug(f'File not found: {file_path}')
            return False
