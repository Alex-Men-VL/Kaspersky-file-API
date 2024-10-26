import abc
import logging
import operator
from functools import cached_property
from pathlib import Path
from typing import Any, Callable

from core.infra.searches.constants import SearchFilterOperatorChoices


logger = logging.getLogger('services')


class BaseSearchFilterHandler(abc.ABC):
    """Абстрактный класс для проведения поиска по фильтру."""

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


class BaseSearchValueFilterHandler(BaseSearchFilterHandler, abc.ABC):
    """Абстрактный класс для проведения поиска по фильтру с одним значением."""

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


class BaseSearchOperatorFilterHandler(BaseSearchFilterHandler, abc.ABC):
    """Абстрактный класс для проведения поиска по фильтру с оператором сравнения."""

    def __init__(self, value: Any, value_operator: str) -> None:
        self.value = value

        self.value_operator = self.operators.get(value_operator)
        if self.value_operator is None:
            raise ValueError(f'Неизвестный оператор сравнения: {value_operator}')

    @cached_property
    def operators(self) -> dict[str, Callable[[Any, Any], bool]]:
        return {
            SearchFilterOperatorChoices.EQUAL.label: operator.eq,
            SearchFilterOperatorChoices.GREATER_THAN.label: operator.gt,
            SearchFilterOperatorChoices.LESS_THAN.label: operator.lt,
            SearchFilterOperatorChoices.GREATER_THAN_EQUAL.label: operator.ge,
            SearchFilterOperatorChoices.LESS_THAN_EQUAL.label: operator.le,
        }
