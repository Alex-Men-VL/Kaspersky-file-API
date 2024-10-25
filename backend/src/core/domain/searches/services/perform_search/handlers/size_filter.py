import logging
from pathlib import Path

from core.domain.searches.services.perform_search.handlers.base import BaseSearchFilterHandler
from core.infra.searches.models import SearchFilter


logger = logging.getLogger('search_handler')


class SizeFilterHandler(BaseSearchFilterHandler):

    @staticmethod
    def can_handle(search_filter: SearchFilter) -> bool:
        return search_filter.size is not None and bool(search_filter.size_operator)

    def handle(self, file_path: Path, search_filter: SearchFilter):
        file_size = file_path.stat().st_size

        comparison = f'{file_size} {search_filter.get_size_operator_display()} {search_filter.size}'

        try:
            return eval(comparison)
        except SyntaxError as e:
            logger.error(f'Ошибка выполнения фильтрации по размеру файла: {e}')
            return False
