import abc
from dataclasses import dataclass

from base.domain.rules import (
    DomainRule,
    IRule,
)
from core.domain.searches.constants import FILTER_VALUE_MUST_HAVE_OPTION_ERROR, FILTER_OPTION_MUST_HAVE_VALUE_ERROR, \
    SIZE_FILTER_MUST_BE_POSITIVE_ERROR
from core.infra.searches.dto import FilterComparableValueDTO


@dataclass(frozen=True)
class FilterValueWithOperatorRule(DomainRule, IRule, abc.ABC):
    filter_label: str

    comparable_value: FilterComparableValueDTO | None = None


@dataclass(frozen=True)
class FilterValueMustHaveOperator(FilterValueWithOperatorRule):
    def is_correct(self) -> bool:
        if self.comparable_value and self.comparable_value.value is not None and not self.comparable_value.operator:
            return False

        return True

    def get_error_message(self) -> str:
        return FILTER_VALUE_MUST_HAVE_OPTION_ERROR.format_map({'label': self.filter_label})


@dataclass(frozen=True)
class FilterOperatorMustHaveValue(FilterValueWithOperatorRule):
    def is_correct(self) -> bool:
        if self.comparable_value and self.comparable_value.operator and self.comparable_value.value is None:
            return False

        return True

    def get_error_message(self) -> str:
        return FILTER_OPTION_MUST_HAVE_VALUE_ERROR.format_map({'label': self.filter_label})


@dataclass(frozen=True)
class SizeFilterMustBePositive(DomainRule, IRule):
    size: int | None = None

    def is_correct(self) -> bool:
        if self.size is not None:
            return self.size > 0
        return True

    def get_error_message(self) -> str:
        return SIZE_FILTER_MUST_BE_POSITIVE_ERROR
