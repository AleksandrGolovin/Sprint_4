import pytest

from data import ( 
    BOOK,
    BOOK_UNKNOWN,
    GENRE_HORROR,
    GENRE_UNKNOWN,
    BOOKS_GENRE
)


class TestBooksCollector:

# ===== add_new_book ==============================================================================================

    def test_add_new_book_correct_book_empty_genre(self, collector_empty):
        """Пустой жанр после добавления"""
        collector_empty.add_new_book(BOOK)

        assert collector_empty.books_genre[BOOK] == '', f'Добавленной книге {BOOK} присвоился не пустой жанр'
    
    @pytest.mark.parametrize('book', ['А', BOOK, 'Б' * 40])
    def test_add_new_book_correct_book_len_one(self, book, collector_empty):
        """Корректная книга добавляется"""
        collector_empty.add_new_book(book)

        assert len(collector_empty.books_genre) == 1, f'При добавлении книги {book} размер коллекции не увеличился'

    def test_add_new_book_correct_named_two_books_len_one(self, collector_empty):
        """Дубликаты не добавляются"""
        collector_empty.add_new_book(BOOK)
        collector_empty.add_new_book(BOOK)

        assert len(collector_empty.books_genre) == 1, f'При повторном добавлении {BOOK} размер коллекции увеличился'

    @pytest.mark.parametrize('book', ['', 'А' * 41])
    def test_add_new_book_incorrect_named_book_len_zero(self, book, collector_empty):
        """Некорректные названия не добавляются"""
        collector_empty.add_new_book(book)

        assert len(collector_empty.books_genre) == 0, f'Книга {book} добавилась в коллекцию, хотя не должна была'

# ===== get_books_genre ===========================================================================================

    def test_get_books_genre_correct_named_book_genre_dict_equal(self, collector_filled):
        """Получение словаря книг-жанров"""
        books_genre = collector_filled.get_books_genre()

        assert books_genre == BOOKS_GENRE, 'Возвращенные методом тестовые данные отличаются от инициализированных'

# ===== get_book_genre ============================================================================================

    def test_get_book_genre_correct_book_genre_true(self, collector_empty):
        """Получение жанра книги"""
        collector_empty.books_genre[BOOK] = GENRE_HORROR
        
        assert collector_empty.get_book_genre(BOOK) == GENRE_HORROR, 'Возвращенные методом тестовые данные отличаются от инициализированных'

# ===== set_book_genre ============================================================================================

    @pytest.mark.parametrize('genre', [GENRE_HORROR, GENRE_UNKNOWN, ''])
    def test_set_book_genre_correct_book_genre_true(self, genre, collector_empty):
        """Установка жанра"""
        collector_empty.books_genre[BOOK] = genre

        collector_empty.set_book_genre(BOOK, GENRE_HORROR)

        assert collector_empty.books_genre[BOOK] == GENRE_HORROR, 'Значение переменной класса отличается от переданного через метод'

# ===== get_books_with_specific_genre =============================================================================

    def test_get_books_with_specific_genre_correct_named_book_genre_dict_correct_genre_success(self, collector_filled):
        """Книги по жанру"""
        books_with_specific_genre_horror = collector_filled.get_books_with_specific_genre(GENRE_HORROR)
        
        assert all(collector_filled.books_genre.get(book) == GENRE_HORROR for book in books_with_specific_genre_horror)

    def test_get_books_with_specific_genre_correct_named_book_genre_dict_incorrect_genre_empty_list(self, collector_filled):
        """Некорректный жанр возвращает пустой список из заполненной коллекции"""
        books_with_specific_genre = collector_filled.get_books_with_specific_genre(GENRE_UNKNOWN)

        assert books_with_specific_genre == []

    @pytest.mark.parametrize('genre', [GENRE_HORROR, GENRE_UNKNOWN])
    def test_get_books_with_specific_genre_empty_books_genre_correct_genre_empty_list(self, genre, collector_empty):
        """Любой жанр возвращает пустой список из пустой коллекции"""
        books_with_specific_genre = collector_empty.get_books_with_specific_genre(genre)

        assert books_with_specific_genre == []

# ===== get_books_for_children ====================================================================================

    def test_get_books_for_children_correct_kids_book_success(self, collector_filled):
        """Детские книги"""
        books_for_children = collector_filled.get_books_for_children()

        assert all(collector_filled.books_genre.get(book) not in collector_filled.genre_age_rating for book in books_for_children)

# ===== add_book_in_favorites =====================================================================================

    @pytest.mark.parametrize('add_tries_count', [1, 2, 3])
    def test_add_book_in_favorites_correct_named_book_several_times_favorites_len_one(self, add_tries_count, collector_filled):
        """Добавление в избранное без дубликатов"""
        for i in range(add_tries_count):
            collector_filled.add_book_in_favorites(BOOK)

        assert len(collector_filled.favorites) == 1

    def test_add_book_in_favorites_unknown_book_empty_favorites(self, collector_filled):
        """Добавление несуществующей книги в избранное"""
        collector_filled.add_book_in_favorites(BOOK_UNKNOWN)

        assert len(collector_filled.favorites) == 0

# ===== delete_book_from_favorites ================================================================================

    def test_delete_book_from_favorites_book_favorites_len_decreased_by_one(self, collector_filled_favorites):
        """Удаление из избранного"""
        len_before = len(collector_filled_favorites.favorites)

        collector_filled_favorites.delete_book_from_favorites(BOOK)
        
        assert len(collector_filled_favorites.favorites) == len_before - 1

    def test_delete_book_from_favorites_unknown_book_favorites_len_not_changed(self, collector_filled_favorites):
        """Удаление неизвестной книги из избранного"""
        len_before = len(collector_filled_favorites.favorites)

        collector_filled_favorites.delete_book_from_favorites(BOOK_UNKNOWN)
        
        assert len(collector_filled_favorites.favorites) == len_before

# ===== get_list_of_favorites_books ===============================================================================

    def test_get_list_of_favorites_books_book_list_equal(self, collector_filled_favorites):
        """Получение списка избранного"""
        list_of_favorites_books = collector_filled_favorites.get_list_of_favorites_books()

        assert set(list_of_favorites_books) == set(collector_filled_favorites.favorites)
