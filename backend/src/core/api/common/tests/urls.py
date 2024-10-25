from uuid import UUID

from django.urls import reverse


def get_search_list_url() -> str:
    return reverse("searches:search-list")


def get_search_detail_url(search_id: UUID) -> str:
    return reverse("searches:search-detail", kwargs={"search_id": search_id})
