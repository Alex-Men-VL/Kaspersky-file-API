from rest_framework import status

from core.api.searches.views import SearchViewSet
from core.infra.baker_recipes import searches_recipes


def test_get_search_detail(api_client, get_search_detail_url):
    search = searches_recipes.search.make()

    response = api_client.get(get_search_detail_url(search.search_id))

    assert response.status_code == status.HTTP_200_OK, response.json()

    expected_result = SearchViewSet.SearchSerializer(search).data

    json_data = response.json()

    assert json_data == expected_result, json_data
