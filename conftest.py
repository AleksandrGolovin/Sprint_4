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
def collector_filled():
    collector_filled = BooksCollector()
    collector_filled.books_genre = BOOKS_GENRE
    return collector_filled

# Экземпляр класса с данными
@pytest.fixture
def collector_filled_favorites():
    collector_filled_favorites = BooksCollector()
    collector_filled_favorites.books_genre = BOOKS_GENRE
    collector_filled_favorites.favorites = list(BOOKS_GENRE)
    return collector_filled_favorites
