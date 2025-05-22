import pytest

from main import BooksCollector


# Экземпляр класса
@pytest.fixture
def collector():
    return BooksCollector()