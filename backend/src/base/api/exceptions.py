from rest_framework import status
from rest_framework.exceptions import APIException


class DomainRuleAPIException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Business logic error.'

    def __init__(self, detail=None):
        self.detail = detail or self.default_detail
