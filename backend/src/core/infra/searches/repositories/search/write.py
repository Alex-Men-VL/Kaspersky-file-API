from uuid import UUID

from base.infra.repositories import BaseWriteRepository
from core.infra.searches.models import Search


class SearchWriteRepository(BaseWriteRepository):
    model = Search

    def create_one(
        self,
        search_filter_id: int,
        finished: bool = False,
    ) -> Search:
        return self.db.create(
            finished=finished,
            search_filter_id=search_filter_id,
        )

    def update_one(
        self,
        pk: UUID,
        finished: bool,
        results: list[str],
    ) -> Search | None:
        self.db.filter(search_id=pk).update(
            finished=finished,
            results=results,
        )
        return self.db.filter(search_id=pk).first()

    def delete_one(self, search_id: UUID) -> None:
        self.db.filter(search_id=search_id).delete()
