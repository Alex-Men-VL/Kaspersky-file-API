class BusinessLogicException(Exception):
    default_message = 'Business logic error'

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(message)


class BusinessRuleTypeException(BusinessLogicException):
    pass


class DomainRuleException(BusinessLogicException):
    pass


class DomainPermissionException(BusinessLogicException):
    pass
