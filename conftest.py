import pytest

from main import BooksCollector
from data import (
    BOOKS_GENRE
)


# Экземпляр класса пустой
@pytest.fixture
def collector_empty():
    collector_empty = BooksCollector()
    return collector_empty

# Экземпляр класса с данными
@pytest.fixture
def collector_filled(collector_empty):
    collector_empty.books_genre = BOOKS_GENRE
    return collector_empty

# Экземпляр класса с данными
@pytest.fixture
def collector_filled_favorites(collector_filled):
    collector_filled.favorites = list(BOOKS_GENRE)
    return collector_filled
