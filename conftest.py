import pytest

from main import BooksCollector
from data import (
    CORRECT_BOOKS_GENRE,
    CORRECT_GENRE_HORROR,
    GENRE_AGE_RATING
)


# Экземпляр класса
@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def books_genre():
    yield CORRECT_BOOKS_GENRE

# Фильтрованный список ужастиков из общего списка
@pytest.fixture
def horrors_books(books_genre):
    yield [book for book, genre in books_genre.items() if genre == CORRECT_GENRE_HORROR]

# Фильтрованный список приемлемых для детей книг из общего списка
@pytest.fixture
def children_allowed_books(books_genre):
    yield [book for book, genre in books_genre.items() if genre not in GENRE_AGE_RATING]