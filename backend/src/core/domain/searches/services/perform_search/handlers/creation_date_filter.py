import logging
import operator
from datetime import datetime
from pathlib import Path

from core.domain.searches.services.perform_search.handlers.base import BaseSearchFilterHandler
from core.infra.searches.constants import SearchFilterOperatorChoices
from core.infra.searches.models import SearchFilter


logger = logging.getLogger('search_handler')


class CreationDateFilterHandler(BaseSearchFilterHandler):

    @staticmethod
    def can_handle(search_filter: SearchFilter) -> bool:
        return search_filter.creation_date is not None and bool(search_filter.creation_date)

    def handle(self, file_path: Path, search_filter: SearchFilter):
        created_at_timestamp = file_path.stat().st_ctime
        created_at = datetime.fromtimestamp(created_at_timestamp)

        operators = {
            SearchFilterOperatorChoices.EQUAL.label: operator.eq,
            SearchFilterOperatorChoices.GREATER_THAN.label: operator.gt,
            SearchFilterOperatorChoices.LESS_THAN.label: operator.lt,
            SearchFilterOperatorChoices.GREATER_THAN_EQUAL.label: operator.ge,
            SearchFilterOperatorChoices.LESS_THAN_EQUAL.label: operator.le,
        }

        creation_date_operator = search_filter.get_creation_date_operator_display()
        date_operator = operators.get(creation_date_operator)

        if date_operator is None:
            logger.error(f'Неизвестный оператор сравнения: {creation_date_operator}')
            return False

        try:
            return date_operator(created_at, search_filter.creation_date)
        except Exception as e:
            logger.error(f'Ошибка выполнения фильтрации по дате создания файла: {e}')
            return False
