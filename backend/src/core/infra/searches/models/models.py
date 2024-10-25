import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models

from base.infra.models import BaseModel

from ..constants import SearchFilterOperatorChoices
from .queryset import SearchManager


class Search(BaseModel):
    search_id = models.UUIDField(
        'Идентификатор запроса',
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    finished = models.BooleanField(
        'Поиск завершен',
        default=False,
    )
    results = ArrayField(
        base_field=models.CharField(max_length=255),
        null=True,
    )
    search_filter = models.OneToOneField(
        'searches.SearchFilter',
        related_name='search',
        on_delete=models.CASCADE,
        null=True,
    )

    objects: SearchManager = SearchManager()

    class Meta:
        verbose_name = 'Поисковой запрос'
        verbose_name_plural = 'Поисковые запросы'

    def __str__(self):
        return self.search_id

    def __repr__(self) -> str:
        return f'<Search(search_id={self.search_id!r})>'


class SearchFilter(BaseModel):
    text = models.TextField(
        'Текст',
        help_text='Текст, который должен содержаться в файле',
        blank=True,
    )
    file_mask = models.CharField(
        'Маска имени файла',
        max_length=255,
        blank=True,
    )

    size = models.PositiveIntegerField(
        'Размер файла',
        null=True,
    )
    size_operator = models.CharField(
        'Оператор сравнения размера',
        choices=SearchFilterOperatorChoices.choices,
        max_length=10,
        blank=True,
    )

    creation_date = models.DateTimeField(
        'Дата создания',
        null=True,
    )
    creation_date_operator = models.CharField(
        'Оператор сравнения размера',
        choices=SearchFilterOperatorChoices.choices,
        max_length=10,
        blank=True,
    )

    class Meta:
        verbose_name = 'Параметры фильтрации'
        verbose_name_plural = 'Параметры фильтрации'

        constraints = [
            models.CheckConstraint(
                condition=(
                    models.Q(size__isnull=True, size_operator__exact='')
                    | models.Q(size__isnull=False, size_operator__isnull=False)
                ),
                name='size_and_operator_both_null_or_both_filled',
            ),
            models.CheckConstraint(
                condition=(
                    models.Q(creation_date__isnull=True, creation_date_operator__exact='')
                    | models.Q(creation_date__isnull=False, creation_date_operator__isnull=False)
                ),
                name='creation_date_and_operator_both_null_or_both_filled',
            ),
        ]
