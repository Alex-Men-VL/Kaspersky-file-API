import fnmatch
from pathlib import Path

from .base import BaseSearchValueFilterHandler


class FileMaskFilterHandler(BaseSearchValueFilterHandler):
    """Класс для проведения поиска по маске имени файла."""

    def handle(self, file_path: Path) -> bool:
        return fnmatch.fnmatch(file_path.name, self.value)
