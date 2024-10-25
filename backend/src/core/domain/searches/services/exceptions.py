class BaseServiceError(Exception):
    pass


class BasePerformSearchServiceError(BaseServiceError):
    pass


class SearchDirectoryNotFoundError(BasePerformSearchServiceError):
    pass
