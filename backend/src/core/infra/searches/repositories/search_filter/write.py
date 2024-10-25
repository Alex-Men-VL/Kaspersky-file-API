from datetime import datetime

from base.infra.repositories import BaseWriteRepository
from core.infra.searches.models import SearchFilter


class SearchFilterWriteRepository(BaseWriteRepository):
    model = SearchFilter

    def create_one(
        self,
        text: str = '',
        file_mask: str = '',
        size: int | None = None,
        size_operator: str = '',
        creation_date: datetime | None = None,
        creation_date_operator: str = '',
    ) -> SearchFilter:
        return self.db.create(
            text=text,
            file_mask=file_mask,
            size=size,
            size_operator=size_operator,
            creation_date=creation_date,
            creation_date_operator=creation_date_operator,
        )

    def update_one(
        self,
        pk: int,
        text: str = '',
        file_mask: str = '',
        size: int | None = None,
        size_operator: str = '',
        creation_date: datetime | None = None,
        creation_date_operator: str = '',
    ) -> SearchFilter | None:
        self.db.filter(pk=pk).update(
            text=text,
            file_mask=file_mask,
            size=size,
            size_operator=size_operator,
            creation_date=creation_date,
            creation_date_operator=creation_date_operator,
        )
        return self.db.filter(pk=pk).first()

    def delete_one(self, pk: int) -> None:
        self.db.filter(pk=pk).delete()
