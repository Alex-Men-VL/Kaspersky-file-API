from core.domain.searches.services.exceptions import BaseServiceError


class BasePerformSearchServiceError(BaseServiceError):
    ...


class SearchDirectoryNotFoundError(BasePerformSearchServiceError):
    ...
