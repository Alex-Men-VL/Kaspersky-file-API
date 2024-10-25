from rest_framework import status

from model_bakery import random_gen

from core.api.common.tests.urls import get_search_list_url
from core.api.searches.views import SearchViewSet
from core.infra.baker_recipes import searches_recipes
from core.infra.searches.repositories.search import search_read_repository


def test_get_searches_list(api_client):
    search_filters = searches_recipes.search_filter.make(
        _quantity=random_gen.gen_integer(2, 6),
        _bulk_create=True,
    )
    searches_recipes.search.make(
        search_filter=iter(search_filters),
        _quantity=len(search_filters),
        _bulk_create=True,
    )

    response = api_client.get(get_search_list_url())

    assert response.status_code == status.HTTP_200_OK, response.json()

    searches = search_read_repository.get_many().with_search_filter().order_by("-created_at")
    expected_result = SearchViewSet.SearchListSerializer(searches, many=True).data

    json_data = response.json()

    assert json_data == expected_result, json_data
