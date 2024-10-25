import logging
import os
from dataclasses import (
    dataclass,
    field,
)
from pathlib import Path

from core.infra.searches.models import Search

from .exceptions import SearchDirectoryNotFoundError
from .handlers.base import BaseSearchFilterHandler
from .handlers.creation_date_filter import CreationDateFilterHandler
from .handlers.file_mask_filter import FileMaskFilterHandler
from .handlers.size_filter import SizeFilterHandler
from .handlers.text_filter import TextFilterHandler


logger = logging.getLogger('tasks')


@dataclass
class PerformSearchService:
    search_dir: str
    search: Search

    max_retries: int = 5
    delay: int = 0.1

    search_handlers: list[BaseSearchFilterHandler] = field(init=False)

    def __post_init__(self):
        search_dir_path = Path(self.search_dir)
        if not (search_dir_path.exists() and search_dir_path.is_dir()):
            raise SearchDirectoryNotFoundError('Search directory does not exist')

        self.search_handlers = self._prepare_handlers()

    def _prepare_handlers(self) -> list[BaseSearchFilterHandler]:
        search_filter = self.search.search_filter
        search_handlers = []
        if search_filter.text:
            search_handlers.append(TextFilterHandler(search_filter.text))

        if search_filter.file_mask:
            search_handlers.append(FileMaskFilterHandler(search_filter.file_mask))

        if search_filter.size and search_filter.size_operator:
            search_handlers.append(
                SizeFilterHandler(
                    value=search_filter.size,
                    value_operator=search_filter.get_size_operator_display(),
                )
            )

        if search_filter.creation_date and search_filter.creation_date_operator:
            search_handlers.append(
                CreationDateFilterHandler(
                    value=search_filter.creation_date,
                    value_operator=search_filter.get_creation_date_operator_display(),
                )
            )

        return search_handlers

    def execute(self) -> None:
        found_files = self._search_files(self.search_dir)

        self.search.results = found_files
        self.search.finished = True
        self.search.save(update_fields=['results', 'finished', 'updated_at'])

    def _search_files(self, directory: str) -> list[Path]:
        found_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = Path(root, file)
                if self._file_matches(file_path):
                    found_files.append(file_path)

        return found_files

    def _file_matches(self, file_path: Path) -> bool:
        for handler in self.search_handlers:
            if not handler.execute(file_path):
                return False

        return True
