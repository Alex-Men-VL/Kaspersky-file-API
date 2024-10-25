from dataclasses import dataclass

from base.domain.rules import (
    DomainRule,
    IRule,
)
from core.domain.searches.constants import (
    SIZE_FILTER_MUST_BE_POSITIVE_ERROR,
)


@dataclass(frozen=True)
class SizeFilterMustBePositive(DomainRule, IRule):
    size: int | None = None

    def is_correct(self) -> bool:
        if self.size is not None:
            return self.size > 0
        return True

    def get_error_message(self) -> str:
        return SIZE_FILTER_MUST_BE_POSITIVE_ERROR
