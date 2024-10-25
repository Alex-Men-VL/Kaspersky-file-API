from django.db.models import TextChoices


class SearchFilterOperatorChoices(TextChoices):
    EQUAL = 'EQ', '=='
    GREATER_THAN = 'GT', '>'
    LESS_THAN = 'LT', '<'
    GREATER_THAN_EQUAL = 'GE', '>='
    LESS_THAN_EQUAL = 'LE', '<='
