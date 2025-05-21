import pytest

from main import BooksCollector


# Экземпляр класса
@pytest.fixture
def collector():
    return BooksCollector()

# Книга с правильным названием
@pytest.fixture
def correct_book():
    return 'Призрак в тостере'

# Правильный жанр
@pytest.fixture
def correct_genre():
    return 'Ужасы'

# Неправильный жанр
@pytest.fixture
def incorrect_genre():
    return 'Триллер'

# Список книг корректной длины
@pytest.fixture
def correct_named_book_list():
    correct_named_book_list = [
        'Гид по выживанию среди андроидов',
        'Как пережить ужин с тещей',
        'Тайна исчезновения кофе в офисе',
        'Приключения плюшевого ленивца в городе',
        'Секреты идеального падения на улице',
        'Коты-марсиане атакуют!',
        'Призрак в тостере',
        'Дело о вечном носке',
        'Ёжик и зомби-морковки',
        'Лягушка-миллионер'
    ]
    return correct_named_book_list

# Словарь книга-жанр с корректными именами
@pytest.fixture
def correct_named_book_genre_dict():
    correct_named_book_genre_dict = {
        'Гид по выживанию среди андроидов': 'Фантастика',
        'Как пережить ужин с тещей': 'Ужасы',
        'Тайна исчезновения кофе в офисе': 'Детективы',
        'Приключения плюшевого ленивца в городе': 'Мультфильмы',
        'Секреты идеального падения на улице': 'Комедии',
        'Коты-марсиане атакуют!': 'Фантастика',
        'Призрак в тостере': 'Ужасы',
        'Дело о вечном носке': 'Детективы',
        'Ёжик и зомби-морковки': 'Мультфильмы',
        'Лягушка-миллионер': 'Комедии'
    }
    return correct_named_book_genre_dict

@pytest.fixture
def genre_age_rating_list():
    genre_age_rating_list = ['Ужасы', 'Детективы']
    return genre_age_rating_list
