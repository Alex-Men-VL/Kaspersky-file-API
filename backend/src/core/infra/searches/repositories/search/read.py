from uuid import UUID

from base.infra.repositories import BaseReadRepository
from core.infra.searches.models.models import Search
from core.infra.searches.models.queryset import SearchQuerySet


class SearchReadRepository(BaseReadRepository):
    model = Search

    def get_one(self, search_id: UUID) -> Search:
        return self.db.get(search_id=search_id)

    def get_last(self) -> Search | None:
        return self.db.last()

    def get_many(self) -> 'SearchQuerySet':
        return self.db.all()

    def get_count(self) -> int:
        return self.db.count()

    def exists(self, search_id: UUID) -> bool:
        return self.db.filter(search_id=search_id).exists()
