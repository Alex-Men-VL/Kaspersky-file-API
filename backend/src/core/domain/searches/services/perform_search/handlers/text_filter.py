import mmap
from pathlib import Path

from .base import BaseSearchValueFilterHandler


class TextFilterHandler(BaseSearchValueFilterHandler):
    """Класс для проведения поиска по содержимому файла."""

    def handle(self, file_path: Path):
        with file_path.open(encoding='utf-8') as fp:
            try:
                with mmap.mmap(fp.fileno(), length=0, access=mmap.ACCESS_READ) as mobj:
                    return self.value.encode('utf-8') in mobj.read()
            except ValueError:
                return False
