import logging
from pathlib import Path

from .base import BaseSearchOperatorFilterHandler


logger = logging.getLogger('search_handler')


class SizeFilterHandler(BaseSearchOperatorFilterHandler):
    """Класс для проведения поиска по размеру файла."""

    def handle(self, file_path: Path) -> bool:
        file_size = file_path.stat().st_size

        size_operator = self.operators.get(self.value_operator)

        if size_operator is None:
            logger.error(f'Неизвестный оператор сравнения: {self.value_operator}')
            return False

        try:
            return size_operator(file_size, self.value)
        except SyntaxError as e:
            logger.error(f'Ошибка выполнения фильтрации по размеру файла: {e}')
            return False
