from django.db import models


class SearchQuerySet(models.QuerySet):
    def new(self) -> 'SearchQuerySet':
        return self.filter(finished=False)


class SearchManager(models.Manager.from_queryset(SearchQuerySet)):  # type: ignore
    ...
