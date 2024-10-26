import logging
from datetime import datetime
from pathlib import Path

from .base import BaseSearchOperatorFilterHandler


logger = logging.getLogger('search_handler')


class CreationDateFilterHandler(BaseSearchOperatorFilterHandler):
    """Класс для проведения поиска по дате создания."""

    def handle(self, file_path: Path) -> bool:
        created_at_timestamp = file_path.stat().st_ctime
        created_at = datetime.fromtimestamp(created_at_timestamp)

        try:
            return self.value_operator(created_at, self.value)
        except Exception as e:
            logger.error(f'Ошибка выполнения фильтрации по дате создания файла: {e}')
            return False
