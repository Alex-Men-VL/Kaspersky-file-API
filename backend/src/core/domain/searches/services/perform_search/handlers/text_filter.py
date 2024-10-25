from pathlib import Path

from core.infra.searches.models import SearchFilter

from .base import BaseSearchFilterHandler


class TextFilterHandler(BaseSearchFilterHandler):
    """Класс для проведения поиска по содержимому файла."""

    @staticmethod
    def can_handle(search_filter: SearchFilter) -> bool:
        return bool(search_filter.text)

    def handle(self, file_path: Path, search_filter: SearchFilter):
        return search_filter.text in file_path.read_text()
