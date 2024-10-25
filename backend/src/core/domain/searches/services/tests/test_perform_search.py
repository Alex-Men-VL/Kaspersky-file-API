from datetime import datetime
from time import sleep

from model_bakery import random_gen

from core.domain.searches.services.perform_search import PerformSearchService
from core.infra.baker_recipes import searches_recipes
from core.infra.searches.constants import SearchFilterOperatorChoices


def test_perform_search_by_text(tmp_path):
    text = 'hello world'
    nested_path = tmp_path / 'test'
    nested_path.mkdir(exist_ok=True)
    # Файлы, не попадающие в критерии поиска
    (tmp_path / 'a.txt').write_text(random_gen.gen_string(100))
    (tmp_path / 'b.txt').write_text(random_gen.gen_string(100))
    (nested_path / 'c.txt').write_text(random_gen.gen_string(100))
    # Файлы, попадающие в критерии поиска
    f1 = tmp_path / 'd.txt'
    f1.write_text(text)
    f2 = nested_path / 'e.txt'
    f2.write_text(text)

    search_filter = searches_recipes.empty_search_filter.make(
        text=text
    )
    search = searches_recipes.search.make(search_filter=search_filter)
    service = PerformSearchService(search_dir=tmp_path)

    service.perform_search(search.search_id)

    search.refresh_from_db()

    assert search.finished
    assert sorted(search.results) == sorted(map(lambda x: x.as_posix(), [f1, f2]))


def test_perform_search_by_file_mask(tmp_path):
    file_mask = '*a*.???'
    nested_path = tmp_path / 'test'
    nested_path.mkdir(exist_ok=True)
    # Файлы, не попадающие в критерии поиска
    (tmp_path / 'cbc.txt').touch()
    (tmp_path / 'bcb.py').touch()
    (nested_path / 'e.txt').touch()
    # Файлы, попадающие в критерии поиска
    f1 = tmp_path / 'a.txt'
    f1.touch()
    f2 = nested_path / 'ba.txt'
    f2.touch()

    search_filter = searches_recipes.empty_search_filter.make(
        file_mask=file_mask
    )
    search = searches_recipes.search.make(search_filter=search_filter)
    service = PerformSearchService(search_dir=tmp_path)

    service.perform_search(search.search_id)

    search.refresh_from_db()

    assert search.finished
    assert sorted(search.results) == sorted(map(lambda x: x.as_posix(), [f1, f2]))


def test_perform_search_by_file_size(tmp_path):
    nested_path = tmp_path / 'test'
    nested_path.mkdir(exist_ok=True)
    # Файлы, не попадающие в критерии поиска
    (tmp_path / 'a.txt').write_text(random_gen.gen_string(100))
    (nested_path / 'b.txt').write_text(random_gen.gen_string(1000))
    # Файл, попадающий в критерий поиска
    f1 = tmp_path / 'c.txt'
    f1.write_text(random_gen.gen_string(500))

    size = f1.stat().st_size

    search_filter = searches_recipes.empty_search_filter.make(
        size=size,
        size_operator=SearchFilterOperatorChoices.EQUAL,
    )
    search = searches_recipes.search.make(search_filter=search_filter)
    service = PerformSearchService(search_dir=tmp_path)

    service.perform_search(search.search_id)

    search.refresh_from_db()

    assert search.finished
    assert search.results == [f1.as_posix()]


def test_perform_search_by_creation_date(tmp_path):
    nested_path = tmp_path / 'test'
    nested_path.mkdir(exist_ok=True)
    # Файлы, не попадающие в критерии поиска
    (tmp_path / 'a.txt').touch()
    (nested_path / 'b.txt').touch()
    # Файл, попадающий в критерий поиска
    sleep(1)
    f1 = tmp_path / 'c.txt'
    f1.touch()

    creation_date = datetime.fromtimestamp(f1.stat().st_ctime)

    search_filter = searches_recipes.empty_search_filter.make(
        creation_date=creation_date,
        creation_date_operator=SearchFilterOperatorChoices.EQUAL,
    )
    search = searches_recipes.search.make(search_filter=search_filter)
    service = PerformSearchService(search_dir=tmp_path)

    service.perform_search(search.search_id)

    search.refresh_from_db()

    assert search.finished
    assert search.results == [f1.as_posix()]
