from typing import Callable
from uuid import UUID

from django.urls import reverse

from rest_framework.test import APIClient

import pytest


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def search_list_url() -> str:
    return reverse('searches:search-list')


@pytest.fixture
def get_search_detail_url() -> Callable[[UUID], str]:
    def inner(search_id: UUID) -> str:
        return reverse('searches:search-detail', kwargs={'search_id': search_id})

    return inner
