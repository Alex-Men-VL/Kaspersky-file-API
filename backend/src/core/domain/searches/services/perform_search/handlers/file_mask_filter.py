import fnmatch
from pathlib import Path

from core.infra.searches.models import SearchFilter

from .base import BaseSearchFilterHandler


class FileMaskFilterHandler(BaseSearchFilterHandler):
    """Класс для проведения поиска по маске имени файла."""

    @staticmethod
    def can_handle(search_filter: SearchFilter) -> bool:
        return bool(search_filter.file_mask)

    def handle(self, file_path: Path, search_filter: SearchFilter):
        return fnmatch.fnmatch(file_path.name, search_filter.file_mask)
