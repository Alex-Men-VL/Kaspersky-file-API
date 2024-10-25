from unittest.mock import patch

import pytest
from rest_framework import status

from model_bakery import random_gen

from core.api.common.tests.urls import get_search_list_url
from core.domain.searches.constants import SIZE_FILTER_MUST_BE_POSITIVE_ERROR
from core.infra.searches.constants import SearchFilterOperatorChoices
from core.infra.searches.repositories.search import search_read_repository


def test_create_search(api_client):
    with patch('core.domain.searches.usecases.create_search.PerformSearchService.run') as mock_create_search:
        mock_create_search.return_value = None

        response = api_client.post(
            get_search_list_url(),
            data={
                'text': random_gen.gen_string(10),
                'file_mask': random_gen.gen_string(10),
                'size': {
                    'value': random_gen.gen_integer(1, 10),
                    'operator': random_gen.gen_from_choices(SearchFilterOperatorChoices.choices)(),
                },
                'creation_time': {
                    'value': random_gen.gen_datetime().date(),
                    'operator': random_gen.gen_from_choices(SearchFilterOperatorChoices.choices)(),
                },
            }
        )

    assert response.status_code == status.HTTP_201_CREATED, response.json()

    search = search_read_repository.get_last()
    expected_result = {
        'search_id': str(search.search_id)
    }

    json_data = response.json()

    assert json_data == expected_result, json_data


@pytest.mark.parametrize(
    ['search_field', 'value'],
    (
        ['size', random_gen.gen_integer(1, 10)],
        ['creation_time', random_gen.gen_datetime().date()]
    ),
    ids=['SIZE', 'CREATION_TIME'],
)
def test_create_search_value_without_operator(api_client, search_field, value):
    data = {
        'text': random_gen.gen_string(10),
        'file_mask': random_gen.gen_string(10),
        search_field: {'value': value},
    }
    
    with patch('core.domain.searches.usecases.create_search.PerformSearchService.run') as mock_create_search:
        mock_create_search.return_value = None

        response = api_client.post(
            get_search_list_url(),
            data=data
        )

    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()


@pytest.mark.parametrize(
    'size_value',
    [0, random_gen.gen_integer(-10, -1)],
    ids=['ZERO_SIZE', 'NEGATIVE_SIZE'],
)
def test_create_search_size_not_positive(api_client, size_value):
    with patch('core.domain.searches.usecases.create_search.PerformSearchService.run') as mock_create_search:
        mock_create_search.return_value = None

        response = api_client.post(
            get_search_list_url(),
            data={
                'text': random_gen.gen_string(10),
                'file_mask': random_gen.gen_string(10),
                'size': {
                    'value': size_value,
                    'operator': random_gen.gen_from_choices(SearchFilterOperatorChoices.choices)(),
                },
            }
        )

    assert response.status_code == status.HTTP_400_BAD_REQUEST, response.json()

    json_data = response.json()

    assert json_data['message'] == SIZE_FILTER_MUST_BE_POSITIVE_ERROR