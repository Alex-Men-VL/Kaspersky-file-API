from dataclasses import (
    dataclass,
    field,
)

from base.domain.rules import IRule
from base.domain.usecases import BaseUseCase
from core.domain.searches.dto import FilterComparableValueDTO
from core.domain.searches.rules import SizeFilterMustBePositive
from core.domain.searches.tasks import perform_search
from core.infra.searches.models import (
    Search,
    SearchFilter,
)


@dataclass(kw_only=True)
class CreateSearchUseCase(BaseUseCase):
    text: str = ''
    file_mask: str = ''

    size: FilterComparableValueDTO = field(default_factory=FilterComparableValueDTO)
    creation_time: FilterComparableValueDTO = field(default_factory=FilterComparableValueDTO)

    def rules(self) -> list[IRule]:
        return [
            SizeFilterMustBePositive(
                size=self.size.value,
            ),
        ]

    def action(self) -> Search:
        search_filter = SearchFilter.objects.create(
            text=self.text,
            file_mask=self.file_mask,
            size=self.size.value,
            size_operator=self.size.operator,
            creation_date=self.creation_time.value,
            creation_date_operator=self.creation_time.operator,
        )

        search = Search.objects.create(search_filter_id=search_filter.pk)

        perform_search(search)

        return search
