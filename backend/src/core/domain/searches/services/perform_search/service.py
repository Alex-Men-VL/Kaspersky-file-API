import logging
import os
import threading
from dataclasses import dataclass, field
from pathlib import Path
from time import sleep

from django.conf import settings

from core.infra.searches.models import Search, SearchFilter

from .exceptions import SearchDirectoryNotFoundError
from .handlers.base import BaseSearchFilterHandler
from .handlers.creation_date_filter import CreationDateFilterHandler
from .handlers.file_mask_filter import FileMaskFilterHandler
from .handlers.size_filter import SizeFilterHandler
from .handlers.text_filter import TextFilterHandler


logger = logging.getLogger('services')


@dataclass
class PerformSearchService:
    search_dir: str

    max_retries: int = 5
    delay: int = 0.1

    search_handlers: list[type[BaseSearchFilterHandler]] = field(init=False)

    def __post_init__(self):
        search_dir_path = Path(self.search_dir)
        if not (search_dir_path.exists() and search_dir_path.is_dir()):
            raise SearchDirectoryNotFoundError('Search directory does not exist')

        self.search_handlers = [
            TextFilterHandler(),
            FileMaskFilterHandler(),
            SizeFilterHandler(),
            CreationDateFilterHandler()
        ]

    def run(self, search_id: int) -> None:
        threading.Thread(target=self._perform_search, args=(search_id,), daemon=True).start()

    def _get_search(self, search_id: int) -> Search:
        for attempt in range(self.max_retries):
            try:
                return Search.objects.get(pk=search_id)
            except Search.DoesNotExist:
                if attempt < self.max_retries - 1:
                    sleep(self.delay)
                    continue

                logger.error(f'Поисковой запрос №{search_id} не найден')
                raise

    def _perform_search(self, search_id: int) -> None:
        logger.info(f'Запуск поиска файлов для {search_id}...')

        search = self._get_search(search_id=search_id)

        found_files = self._search_files(self.search_dir, search.search_filter)

        search.results = found_files
        search.finished = True
        search.save(update_fields=['results', 'finished', 'updated_at'])

        logger.info(f'Конец поиска файлов для {search.search_id}')

    def _search_files(self, directory: str, search_filter: SearchFilter):
        found_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = Path(root, file)
                if self._file_matches(file_path, search_filter):
                    found_files.append(file_path)

        return found_files

    def _file_matches(self, file_path: Path, search_filter: SearchFilter):
        for handler in self.search_handlers:
            if not handler.execute(file_path, search_filter):
                return False

        return True
