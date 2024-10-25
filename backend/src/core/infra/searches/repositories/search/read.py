from uuid import UUID

from django.db.models import QuerySet

from base.infra.repositories import BaseReadRepository
from core.infra.searches.models.models import Search
from core.infra.searches.models.queryset import SearchQuerySet


class SearchReadRepository(BaseReadRepository):
    model = Search

    def get_one(self, search_id: UUID) -> Search | None:
        return self.db.filter(search_id=search_id).first()

    def get_many(self) -> 'SearchQuerySet':
        return self.db.all()

    def get_count(self) -> int:
        return self.db.count()

    def exists(self, search_id: UUID) -> bool:
        return self.db.filter(search_id=search_id).exists()
