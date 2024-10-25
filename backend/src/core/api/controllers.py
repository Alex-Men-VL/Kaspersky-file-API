from functools import wraps

from rest_framework import exceptions

from base.api.exceptions import DomainRuleAPIException
from base.domain.exceptions import (
    DomainPermissionException,
    DomainRuleException,
)


def catch_use_case_errors_as_view(method):
    """Декоратор для обработки ошибок из UseCase, при вызове их из ViewSet, и конвертации в ошибку DRF."""

    @wraps(method)
    def wrapper(request, *args, **kwargs):
        try:
            return method(request, *args, **kwargs)
        except DomainRuleException as ex:
            raise DomainRuleAPIException(
                detail={
                    'message': ex.message,
                },
            )
        except DomainPermissionException as ex:
            raise exceptions.PermissionDenied(detail=ex.message)

    return wrapper
