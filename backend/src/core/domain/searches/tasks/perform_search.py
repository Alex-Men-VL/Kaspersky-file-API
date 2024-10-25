import logging

from django.conf import settings

from huey.contrib.djhuey import on_commit_task

from core.domain.searches.services.perform_search import PerformSearchService
from core.infra.searches.models import Search


logger = logging.getLogger('tasks')


@on_commit_task()
def perform_search(search: Search) -> None:
    logger.info(f'Запуск поиска файлов для {search.search_id}...')

    service = PerformSearchService(search_dir=settings.SEARCH_DIRECTORY, search=search)
    service.execute()

    logger.info(f'Конец поиска файлов для {search.search_id}')
