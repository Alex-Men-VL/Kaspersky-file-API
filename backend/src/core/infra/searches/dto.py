from dataclasses import dataclass
from typing import Any

from base.infra.dto import FromDictMixin


@dataclass
class FilterComparableValueDTO(FromDictMixin):
    value: Any = None
    operator: str = ''
