import threading
from dataclasses import dataclass, InitVar, field
from time import sleep

from django.conf import settings

from base.domain.rules import IRule
from base.domain.usecases import BaseUseCase
from core.domain.searches.rules import FilterValueMustHaveOperator, FilterOperatorMustHaveValue, \
    SizeFilterMustBePositive
from core.domain.searches.services.perform_search import PerformSearchService
from core.infra.searches.dto import FilterComparableValueDTO
from core.infra.searches.models import Search
from core.infra.searches.repositories.search import search_write_repository
from core.infra.searches.repositories.search_filter import search_filter_write_repository


@dataclass(kw_only=True)
class CreateSearchUseCase(BaseUseCase):
    text: str = ''
    file_mask: str = ''

    default_size: InitVar[dict | None] = None
    default_creation_time: InitVar[dict | None] = None

    size: FilterComparableValueDTO | None = field(init=False, default_factory=FilterComparableValueDTO)
    creation_time: FilterComparableValueDTO | None = field(init=False, default_factory=FilterComparableValueDTO)

    def __post_init__(self, default_size: dict | None, default_creation_time: dict | None):
        if default_size and isinstance(default_size, dict):
            self.size = FilterComparableValueDTO.from_dict(default_size)
            
        if default_creation_time and isinstance(default_creation_time, dict):
            self.creation_time = FilterComparableValueDTO.from_dict(default_creation_time)

    def rules(self) -> list[IRule]:
        return [
            FilterValueMustHaveOperator(
                filter_label='Размер',
                comparable_value=self.size,
            ),
            FilterOperatorMustHaveValue(
                filter_label='Размер',
                comparable_value=self.size,
            ),

            FilterValueMustHaveOperator(
                filter_label='Дата создания',
                comparable_value=self.creation_time,
            ),
            FilterOperatorMustHaveValue(
                filter_label='Дата создания',
                comparable_value=self.creation_time,
            ),
            SizeFilterMustBePositive(
                size=self.size.value,
            )
        ]

    def action(self) -> Search:
        search_filter = search_filter_write_repository.create_one(
            text=self.text,
            file_mask=self.file_mask,
            size=self.size.value,
            size_operator=self.size.operator,
            creation_date=self.creation_time.value,
            creation_date_operator=self.creation_time.operator,
        )

        search = search_write_repository.create_one(search_filter_id=search_filter.pk)

        PerformSearchService(search_dir=settings.SEARCH_DIRECTORY).run(search.pk)

        return search
