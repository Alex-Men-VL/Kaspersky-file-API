class BaseServiceError(Exception):
    ...


class BasePerformSearchServiceError(BaseServiceError):
    ...


class SearchDirectoryNotFoundError(BasePerformSearchServiceError):
    ...
