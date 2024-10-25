from django.db import models


class SearchQuerySet(models.QuerySet):
    def with_search_filter(self) -> 'SearchQuerySet':
        return self.select_related('search_filter')


class SearchManager(models.Manager.from_queryset(SearchQuerySet)):  # type: ignore
    ...
