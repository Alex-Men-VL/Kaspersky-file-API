from django.db.models import QuerySet

from base.infra.repositories import BaseReadRepository
from core.infra.searches.models import SearchFilter


class SearchFilterReadRepository(BaseReadRepository):
    model = SearchFilter

    def get_one(self, id: int) -> SearchFilter | None:
        return self.db.filter(id=id).first()

    def get_many(self) -> 'QuerySet':
        return self.db.all()

    def get_count(self) -> int:
        return self.db.count()

    def exists(self, id: int) -> bool:
        return self.db.filter(id=id).exists()
