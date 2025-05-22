import pytest

from data import ( 
    CORRECT_BOOK,
    UNKNOWN_BOOK,
    CORRECT_GENRE_HORROR,
    INCORRECT_GENRE
)


class TestBooksCollector:

# ===== add_new_book ==============================================================================================

    def test_add_new_book_correct_book_empty_genre(self, collector):
        """Пустой жанр после добавления"""
        # Arrange
        book = CORRECT_BOOK

        # Act
        collector.add_new_book(book)

        # Assert
        assert collector.books_genre[book] == '', f'Добавленной книге {book} присвоился не пустой жанр'
    
    @pytest.mark.parametrize('book', ['А', CORRECT_BOOK, 'Б' * 40])
    def test_add_new_book_correct_book_len_one(self, book, collector):
        """Корректная книга добавляется"""
        collector.add_new_book(book)

        assert len(collector.books_genre) == 1, f'При добавлении книги {book} размер коллекции не увеличился'

    def test_add_new_book_correct_named_two_books_len_one(self, collector):
        """Дубликаты не добавляются"""
        book = CORRECT_BOOK

        collector.add_new_book(book)
        collector.add_new_book(book)

        assert len(collector.books_genre) == 1, f'При повторном добавлении {book} размер коллекции увеличился'

    @pytest.mark.parametrize('book', ['', 'А' * 41])
    def test_add_new_book_incorrect_named_book_len_zero(self, book, collector):
        """Некорректные названия не добавляются"""
        collector.add_new_book(book)

        assert len(collector.books_genre) == 0, f'Книга {book} добавилась в коллекцию, хотя не должна была'

# ===== get_books_genre ===========================================================================================

    def test_get_books_genre_correct_named_book_genre_dict_equal(self, collector, books_genre):
        """Получение словаря книг-жанров"""
        collector.books_genre=books_genre

        assert collector.get_books_genre() == books_genre, 'Возвращенные методом тестовые данные отличаются от инициализированных'

# ===== get_book_genre ============================================================================================

    def test_get_book_genre_correct_book_genre_true(self, collector):
        """Получение жанра книги"""
        book = CORRECT_BOOK
        genre = CORRECT_GENRE_HORROR

        collector.books_genre[book] = genre
        
        assert collector.get_book_genre(book) == genre, 'Возвращенные методом тестовые данные отличаются от инициализированных'

# ===== set_book_genre ============================================================================================

    @pytest.mark.parametrize('genre', [CORRECT_GENRE_HORROR, INCORRECT_GENRE, ''])
    def test_set_book_genre_correct_book_genre_true(self, genre, collector):
        """Установка жанра"""
        book = CORRECT_BOOK
        correct_genre = CORRECT_GENRE_HORROR
        collector.books_genre[book] = genre

        collector.set_book_genre(book, correct_genre)

        assert collector.books_genre[book] == correct_genre, 'Значение переменной класса отличается от переданного через метод'

# ===== get_books_with_specific_genre =============================================================================

    def test_get_books_with_specific_genre_correct_named_book_genre_dict_correct_genre_equal(self, collector, books_genre, horrors_books):
        """Книги по жанру"""
        genre_horror = CORRECT_GENRE_HORROR
        collector.books_genre = books_genre

        books_with_specific_genre_horror = collector.get_books_with_specific_genre(genre_horror)
        
        assert set(horrors_books) == set(books_with_specific_genre_horror)

    def test_get_books_with_specific_genre_correct_named_book_genre_dict_incorrect_genre_empty_list(self, collector, books_genre):
        """Некорректный жанр возвращает пустой список"""
        incorrent_genre = INCORRECT_GENRE
        collector.books_genre = books_genre

        books_with_specific_genre = collector.get_books_with_specific_genre(incorrent_genre)

        assert books_with_specific_genre == []

    def test_get_books_with_specific_genre_empty_books_genre_correct_genre_empty_list(self, collector):
        """Корректный жанр возвращает пустой список из пустой коллекции"""
        genre = CORRECT_GENRE_HORROR

        books_with_specific_genre = collector.get_books_with_specific_genre(genre)

        assert books_with_specific_genre == []

# ===== get_books_for_children ====================================================================================

    def test_get_books_for_children_correct_kids_book_equal(self, collector, books_genre, children_allowed_books):
        """Детские книги"""
        collector.books_genre = books_genre

        books_for_children = collector.get_books_for_children()

        assert set(children_allowed_books) == set(books_for_children)

# ===== add_book_in_favorites =====================================================================================

    def test_add_book_in_favorites_correct_named_one_book_favorites_len_one(self, collector):
        """Добавление в избранное"""
        book = CORRECT_BOOK
        genre = CORRECT_GENRE_HORROR
        collector.books_genre[book] = genre

        collector.add_book_in_favorites(book)

        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_correct_named_two_same_book_favorites_len_one(self, collector):
        """Дубликаты в избранном"""
        book = CORRECT_BOOK
        genre = CORRECT_GENRE_HORROR
        collector.books_genre[book] = genre

        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)

        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_one_book_not_in_collector_empty_favorites(self, collector, books_genre):
        """Добавление несуществующей книги в избранное"""
        unknown_book = UNKNOWN_BOOK
        collector.books_genre = books_genre

        collector.add_book_in_favorites(unknown_book)

        assert len(collector.favorites) == 0

# ===== delete_book_from_favorites ================================================================================

    def test_delete_book_from_favorites_exists_book_empty_favorites(self, collector):
        """Удаление из избранного"""
        book = CORRECT_BOOK
        collector.favorites = [book]

        collector.delete_book_from_favorites(book)
        
        assert collector.favorites == []

    def test_delete_book_from_favorites_unknown_book_favorites_lists_not_changed(self, collector, books_genre):
        """Удаление неизвестной книги из избранного"""
        unknown_book = UNKNOWN_BOOK
        collector.favorites = books_genre.keys()
        
        collector.delete_book_from_favorites(unknown_book)
        
        assert set(collector.favorites) == set(books_genre.keys())

# ===== get_list_of_favorites_books ===============================================================================

    def test_get_list_of_favorites_books_book_list_equal(self, collector, books_genre):
        """Получение списка избранного"""
        collector.favorites = books_genre.keys()

        list_of_favorites_books = collector.get_list_of_favorites_books()

        assert set(list_of_favorites_books) == set(books_genre.keys())
