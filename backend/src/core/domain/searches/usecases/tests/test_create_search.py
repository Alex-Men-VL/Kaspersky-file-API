from unittest.mock import patch

import pytest

from model_bakery import random_gen

from base.domain.exceptions import DomainRuleException
from core.domain.searches.constants import SIZE_FILTER_MUST_BE_POSITIVE_ERROR
from core.domain.searches.usecases.create_search import CreateSearchUseCase
from core.infra.searches.constants import SearchFilterOperatorChoices


def test_create_search():
    use_case = CreateSearchUseCase(
        text=random_gen.gen_string(10),
        file_mask=random_gen.gen_string(10),
        default_size={
            'value': random_gen.gen_integer(1, 10),
            'operator': random_gen.gen_from_choices(SearchFilterOperatorChoices.choices)(),
        },
        default_creation_time={
            'value': random_gen.gen_datetime(),
            'operator': random_gen.gen_from_choices(SearchFilterOperatorChoices.choices)(),
        },
    )

    with patch('core.domain.searches.usecases.create_search.PerformSearchService.run') as mock_create_search:
        mock_create_search.return_value = None

        search = use_case.execute()

    assert search
    assert search.search_filter
    assert not search.finished
    assert not search.results


@pytest.mark.parametrize(
    'size_value',
    [0, random_gen.gen_integer(-10, -1)],
    ids=['ZERO_SIZE', 'NEGATIVE_SIZE'],
)
def test_create_search_size_not_positive(size_value):
    use_case = CreateSearchUseCase(
        text=random_gen.gen_string(10),
        file_mask=random_gen.gen_string(10),
        default_size={
            'value': size_value,
            'operator': random_gen.gen_from_choices(SearchFilterOperatorChoices.choices)(),
        },
    )
    with patch('core.domain.searches.usecases.create_search.PerformSearchService.run') as mock_create_search:
        mock_create_search.return_value = None

        with pytest.raises(DomainRuleException) as exc:
            use_case.execute()

    assert str(exc.value) == SIZE_FILTER_MUST_BE_POSITIVE_ERROR
