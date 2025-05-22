import pytest

from data import (
    CORRECT_NAMED_BOOK_GENRE_DICT, 
    CORRECT_BOOK, INCORRECT_BOOK,
    CORRECT_GENRE, INCORRECT_GENRE,
    GENRE_AGE_RATING
)


class TestBooksCollector:

# ===============================================================================================================

    # Книга с корректным названием добавляется в список
    def test_add_new_book_correct_book_true(self, collector):
        collector.add_new_book(CORRECT_BOOK)

        assert len(collector.books_genre) == 1 and CORRECT_BOOK in collector.books_genre

    # Книга с корректным названием добавляются в список
    def test_add_new_book_correct_book_empty_genre(self, collector):
        collector.add_new_book(CORRECT_BOOK)

        assert collector.books_genre[CORRECT_BOOK] == ''

    # Две одинаковые книги корретной длины, добавляется только одна
    def test_add_new_book_correct_named_two_books_len_one(self, collector):
        collector.add_new_book(CORRECT_BOOK)
        collector.add_new_book(CORRECT_BOOK)

        assert len(collector.books_genre) == 1 and CORRECT_BOOK in collector.books_genre

    # Книги с некорректным названием не добавляются
    @pytest.mark.parametrize('name', ['', 'Как не потеряться в Икеа и найти выход до пенсии'])
    def test_add_new_book_incorrect_named_book_len_zero(self, collector, name):
        collector.add_new_book(name)

        assert len(collector.books_genre) == 0

# ===============================================================================================================

    # Полученный словарь книга-жанр идентичен по значениям инициализированному
    def test_get_books_genre_correct_named_book_genre_dict_equal(self, collector, correct_named_book_genre_dict):
        collector.books_genre=correct_named_book_genre_dict

        assert collector.get_books_genre() == correct_named_book_genre_dict  # Python 3.7+

# ===============================================================================================================

    # Полученный жанр книги совпадает с инициализированным
    def test_get_book_genre_correct_book_genre_true(self, collector):
        collector.books_genre[CORRECT_BOOK] = CORRECT_GENRE
        
        assert collector.get_book_genre(CORRECT_BOOK) == CORRECT_GENRE

# ===============================================================================================================

    # Жанр книги устанавливается корректно, если книга есть в коллекции
    @pytest.mark.parametrize('genre', [CORRECT_GENRE, INCORRECT_GENRE, ''])
    def test_set_book_genre_correct_book_genre_true(self, genre, collector):
        collector.books_genre[CORRECT_BOOK] = genre
        collector.set_book_genre(CORRECT_BOOK, CORRECT_GENRE)

        assert collector.books_genre[CORRECT_BOOK] == CORRECT_GENRE

# ===============================================================================================================

    # Проверка получения книг определенного жанра со списком корректных жанров
    def test_get_books_with_specific_genre_correct_named_book_genre_dict_correct_genre_equal(self, collector):
        collector.books_genre = CORRECT_NAMED_BOOK_GENRE_DICT
        filtered_correct_named_book = [book for book, genre in CORRECT_NAMED_BOOK_GENRE_DICT.items() if genre == CORRECT_GENRE]
        
        assert set(filtered_correct_named_book) == set(collector.get_books_with_specific_genre(CORRECT_GENRE))

    # Проверка получения книг определенного жанра со списком некорректных жанров
    def test_get_books_with_specific_genre_correct_named_book_genre_dict_incorrect_genre_empty_list(self, collector):
        collector.books_genre = CORRECT_NAMED_BOOK_GENRE_DICT

        assert collector.get_books_with_specific_genre(INCORRECT_GENRE) == []

    # Проверка получения книг определенного жанра со списком корректных жанров и с пустым словарем книга-жанр
    def test_get_books_with_specific_genre_empty_books_genre_correct_genre_empty_list(self, collector):
        
        assert collector.get_books_with_specific_genre(CORRECT_GENRE) == []

# ===============================================================================================================

    # Проверка получения книг детского рейтинга со списком взрослых жанров
    def test_get_books_for_children_correct_kids_book_equal(self, collector):
        collector.books_genre = CORRECT_NAMED_BOOK_GENRE_DICT
        filtered_books = [book_name for book_name, book_genre in CORRECT_NAMED_BOOK_GENRE_DICT.items() if book_genre not in GENRE_AGE_RATING]

        assert set(filtered_books) == set(collector.get_books_for_children())

# ===============================================================================================================

    # Проверка добавления книги в избранное, если книга уже есть в коллекции
    def test_add_book_in_favorites_correct_named_one_book_favorites_len_one(self, collector):
        collector.books_genre[CORRECT_BOOK] = CORRECT_GENRE
        collector.add_book_in_favorites(CORRECT_BOOK)

        assert len(collector.favorites) == 1 and CORRECT_BOOK in collector.favorites

    # Проверка добавления двух одинаковых книг в избранное, если книга уже есть в коллекции
    def test_add_book_in_favorites_correct_named_two_same_book_favorites_len_one(self, collector):
        collector.books_genre[CORRECT_BOOK] = CORRECT_GENRE
        collector.add_book_in_favorites(CORRECT_BOOK)
        collector.add_book_in_favorites(CORRECT_BOOK)

        assert len(collector.favorites) == 1 and CORRECT_BOOK in collector.favorites

    # Проверка добавления в избранное книги, которой нет в коллекции
    def test_add_book_in_favorites_one_book_not_in_collector_empty_favorites(self, collector):
        collector.books_genre = CORRECT_NAMED_BOOK_GENRE_DICT
        collector.add_book_in_favorites(INCORRECT_BOOK)

        assert len(collector.favorites) == 0

# ===============================================================================================================

    # Удаление из избранного книги, которая там есть
    def test_delete_book_from_favorites_exists_book_empty_favorites(self, collector):
        collector.favorites.append(CORRECT_BOOK)
        collector.delete_book_from_favorites(CORRECT_BOOK)
        
        assert collector.favorites == []


    # Удаление из избранного книги, которой там нет
    def test_delete_book_from_favorites_not_exists_book_favorites_lists_not_changed(self, collector, correct_named_book_list):
        collector.favorites = correct_named_book_list
        collector.delete_book_from_favorites(INCORRECT_BOOK)
        
        assert set(collector.favorites) == set(correct_named_book_list)

# ===============================================================================================================

    # Получение списка избранного и сравнение с инициализируемым
    def test_get_list_of_favorites_books_book_list_equal(self, collector, correct_named_book_list):
        collector.favorites = CORRECT_NAMED_BOOK_GENRE_DICT.keys()

        assert set(collector.get_list_of_favorites_books()) == set(CORRECT_NAMED_BOOK_GENRE_DICT.keys())

# ===============================================================================================================
