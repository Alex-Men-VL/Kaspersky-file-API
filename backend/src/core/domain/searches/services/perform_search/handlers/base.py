import abc
import logging
import operator
from functools import cached_property
from pathlib import Path
from typing import Any

from core.infra.searches.constants import SearchFilterOperatorChoices


logger = logging.getLogger('services')


class BaseSearchFilterHandler(abc.ABC):
    """Абстрактный класс для проведения поиска по определенному фильтру."""

    def __init__(self, value: Any) -> None:
        self.value = value

    @abc.abstractmethod
    def handle(self, file_path: Path) -> bool:
        """Выполняет непосредственные действие фильтра."""

        raise NotImplementedError

    def execute(self, file_path: Path) -> bool:
        try:
            return self.handle(file_path)
        except FileNotFoundError:
            logger.debug(f'File not found: {file_path}')
            return False


class BaseSearchOperatorFilterHandler(abc.ABC):
    """Абстрактный класс для проведения поиска по определенному фильтру."""

    def __init__(self, value: Any, value_operator: str) -> None:
        self.value = value
        if value_operator not in self.operators:
            raise ValueError(f'Неизвестный оператор сравнения: {value_operator}')

        self.value_operator = value_operator

    @cached_property
    def operators(self) -> dict:
        return {
            SearchFilterOperatorChoices.EQUAL.label: operator.eq,
            SearchFilterOperatorChoices.GREATER_THAN.label: operator.gt,
            SearchFilterOperatorChoices.LESS_THAN.label: operator.lt,
            SearchFilterOperatorChoices.GREATER_THAN_EQUAL.label: operator.ge,
            SearchFilterOperatorChoices.LESS_THAN_EQUAL.label: operator.le,
        }

    @abc.abstractmethod
    def handle(self, file_path: Path) -> bool:
        """Выполняет непосредственные действие фильтра."""

        raise NotImplementedError

    def execute(self, file_path: Path) -> bool:
        try:
            return self.handle(file_path)
        except FileNotFoundError:
            logger.debug(f'File not found: {file_path}')
            return False
