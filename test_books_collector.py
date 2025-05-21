import pytest

from main import BooksCollector


class TestBooksCollector:

    # Тестовые данные для параметризации: пары книга-жанр
    correct_named_book_genre_list = [
        ['Гид по выживанию среди андроидов', 'Фантастика'],
        ['Как пережить ужин с тещей', 'Ужасы'],
        ['Тайна исчезновения кофе в офисе', 'Детективы'],
        ['Приключения плюшевого ленивца в городе', 'Мультфильмы'],
        ['Секреты идеального падения на улице', 'Комедии'],
        ['Коты-марсиане атакуют!', 'Фантастика'],
        ['Призрак в тостере', 'Ужасы'],
        ['Дело о вечном носке', 'Детективы'],
        ['Ёжик и зомби-морковки', 'Мультфильмы'],
        ['Лягушка-миллионер', 'Комедии']
    ]

    # Тестовые данные для параметризации: корректные жанры
    correct_genre_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    
    # Тестовые данные для параметризации: некорректные жанры
    incorrect_genre_list = ['Саморазвитие', 'Кулинария', 'Поэзия', 'История', 'Психология']

    # Тестовые данные для параметризации: некорректные жанры
    correct_kids_genre_list = ['Фантастика', 'Мультфильмы', 'Комедии']

    # Тестовые данные для параметризации: некорректные жанры
    incorrect_kids_genre_list = ['Ужасы', 'Детективы']

    # Две книги корретной длины названия добавляются в список
    def test_add_new_book_correct_named_books_len_increased(self, collector, correct_named_book_list):
        current_len = len(collector.books_genre)
        input_len = len(correct_named_book_list)

        for name in correct_named_book_list:
            collector.add_new_book(name)

        assert len(collector.books_genre) == current_len + input_len

    # Книги с некорректным названием не добавляются
    @pytest.mark.parametrize('name', ['', 'Как не потеряться в Икеа и найти выход до пенсии'])
    def test_add_new_book_incorrect_named_len_zero(self, collector, name):
        collector.add_new_book(name)

        assert len(collector.books_genre) == 0

    # Полученный словарь книга-жанр идентичен по значениям переданному словарю
    def test_get_books_genre_correct_named_book_genre_dict_true(self, collector, correct_named_book_genre_dict):
        collector.books_genre=correct_named_book_genre_dict

        assert collector.get_books_genre() == correct_named_book_genre_dict  # Python 3.7+

    # Получение жанра по имени
    @pytest.mark.parametrize('name, genre', correct_named_book_genre_list)
    def test_get_book_genre_correct_named_book_genre_true(self, collector, name, genre):
        collector.books_genre[name] = genre
        
        assert collector.get_book_genre(name) == genre

    # Установка жанра для книги
    @pytest.mark.parametrize('name, genre', correct_named_book_genre_list)
    def test_set_book_genre_correct_named_book_genre_true(self, collector, name, genre):
        collector.books_genre[name] = ''
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    # Проверка получения книг определенного жанра со списком корректных жанров
    @pytest.mark.parametrize('genre', correct_genre_list)
    def test_get_books_with_specific_genre_correct_named_book_genre_dict_and_correct_genre_true(self, collector, genre, correct_named_book_genre_dict):
        collector.books_genre = correct_named_book_genre_dict
        filtered_books = [book_name for book_name, book_genre in correct_named_book_genre_dict.items() if book_genre == genre]

        assert filtered_books == collector.get_books_with_specific_genre(genre)

    # Проверка получения книг определенного жанра со списком некорректных жанров
    @pytest.mark.parametrize('genre', incorrect_genre_list)
    def test_get_books_with_specific_genre_correct_named_book_genre_dict_and_incorrect_genre_empty_list(self, collector, genre, correct_named_book_genre_dict):
        collector.books_genre = correct_named_book_genre_dict

        assert collector.get_books_with_specific_genre(genre) == []

    # Проверка получения книг определенного жанра со списком корректных жанров и с пустым словарем книга-жанр
    @pytest.mark.parametrize('genre', correct_genre_list)
    def test_get_books_with_specific_genre_without_book_genre_dict_and_correct_genre_empty_list(self, collector, genre):
        collector.books_genre = {}
        
        assert collector.get_books_with_specific_genre(genre) == []

    # Проверка получения книг детского рейтинга со списком корректных детских жанров и списком взрослых жанров
    @pytest.mark.parametrize('genre', correct_kids_genre_list)
    def test_get_books_for_children_correct_kids_genre_and_genre_age_rating_list_true(self, genre, collector, correct_named_book_genre_dict, genre_age_rating_list):
        collector.books_genre = correct_named_book_genre_dict
        filtered_books = [book_name for book_name, book_genre in correct_named_book_genre_dict.items() if book_genre not in genre_age_rating_list]

        assert filtered_books == collector.get_books_for_children()