from core.domain.searches.services.exceptions import BaseServiceError


class BasePerformSearchServiceError(BaseServiceError):
    pass


class SearchDirectoryNotFoundError(BasePerformSearchServiceError):
    pass
