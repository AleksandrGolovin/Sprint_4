import pytest

from main import BooksCollector

# Фабрика для создания коллектора: пустого, с книгами и/или с избранным
@pytest.fixture
def collector_factory():
    def _factory(books=None, favorites=None):
        collector = BooksCollector()
        if books:
            collector.books_genre = books
        if favorites:
            collector.favorites = favorites
        return collector
    return _factory
