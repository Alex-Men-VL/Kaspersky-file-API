from model_bakery import random_gen
from model_bakery.recipe import (
    foreign_key,
    Recipe,
)

from .constants import SearchFilterOperatorChoices
from .models import (
    Search,
    SearchFilter,
)


empty_search_filter = Recipe(SearchFilter)

search_filter = empty_search_filter.extend(
    text=random_gen.gen_string(10),
    file_mask=random_gen.gen_string(10),
    size=random_gen.gen_integer(1, 10),
    size_operator=random_gen.gen_from_choices(SearchFilterOperatorChoices.choices),
    creation_date=random_gen.gen_datetime(),
    creation_date_operator=random_gen.gen_from_choices(SearchFilterOperatorChoices.choices),
)

search = Recipe(
    Search,
    search_filter=foreign_key(search_filter),
)
