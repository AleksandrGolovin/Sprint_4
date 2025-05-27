import pytest

from data import ( 
    BOOK_HORROR,
    BOOK_UNKNOWN,
    GENRE_HORROR,
    GENRE_UNKNOWN,
    BOOKS_GENRE
)


class TestBooksCollector:

# ===== add_new_book ==============================================================================================

    def test_add_new_book_correct_book_empty_genre(self, collector_factory):
        """Пустой жанр после добавления"""
        collector = collector_factory()

        collector.add_new_book(BOOK_HORROR)

        assert collector.books_genre[BOOK_HORROR] == '', f'Добавленной книге {BOOK_HORROR} присвоился не пустой жанр'
    
    @pytest.mark.parametrize('book', ['А', BOOK_HORROR, 'Б' * 40])
    def test_add_new_book_correct_book_len_one(self, book, collector_factory):
        """Корректная книга добавляется"""
        collector = collector_factory()

        collector.add_new_book(book)

        assert len(collector.books_genre) == 1, f'При добавлении книги {book} размер коллекции не увеличился'

    def test_add_new_book_correct_named_two_books_len_one(self, collector_factory):
        """Дубликаты не добавляются"""
        collector = collector_factory()

        collector.add_new_book(BOOK_HORROR)
        collector.add_new_book(BOOK_HORROR)

        assert len(collector.books_genre) == 1, f'При повторном добавлении {BOOK_HORROR} размер коллекции увеличился'

    @pytest.mark.parametrize('book', ['', 'А' * 41])
    def test_add_new_book_incorrect_named_book_len_zero(self, book, collector_factory):
        """Некорректные названия не добавляются"""
        collector = collector_factory()

        collector.add_new_book(book)

        assert len(collector.books_genre) == 0, f'Книга {book} добавилась в коллекцию, хотя не должна была'

# ===== get_books_genre ===========================================================================================

    def test_get_books_genre_correct_named_book_genre_dict_equal(self, collector_factory):
        """Получение словаря книг-жанров"""
        collector = collector_factory(books=BOOKS_GENRE)

        assert collector.get_books_genre() == BOOKS_GENRE

# ===== get_book_genre ============================================================================================

    def test_get_book_genre_correct_book_genre_true(self, collector_factory):
        """Получение жанра книги"""
        collector = collector_factory(books={BOOK_HORROR: GENRE_HORROR})
        
        assert collector.get_book_genre(BOOK_HORROR) == GENRE_HORROR

# ===== set_book_genre ============================================================================================

    @pytest.mark.parametrize('genre', [GENRE_HORROR, GENRE_UNKNOWN, ''])
    def test_set_book_genre_correct_book_genre_true(self, genre, collector_factory):
        """Установка жанра"""
        collector = collector_factory(books={BOOK_HORROR: genre})

        collector.set_book_genre(BOOK_HORROR, GENRE_HORROR)

        assert collector.books_genre[BOOK_HORROR] == GENRE_HORROR

# ===== get_books_with_specific_genre =============================================================================

    def test_get_books_with_specific_genre_correct_named_book_genre_dict_correct_genre_success(self, collector_factory):
        """Книги по жанру"""
        collector = collector_factory(books=BOOKS_GENRE)

        books_with_specific_genre_horror = collector.get_books_with_specific_genre(GENRE_HORROR)
        
        assert all(collector.books_genre.get(book) == GENRE_HORROR for book in books_with_specific_genre_horror)

    def test_get_books_with_specific_genre_correct_named_book_genre_dict_incorrect_genre_empty_list(self, collector_factory):
        """Некорректный жанр возвращает пустой список из заполненной коллекции"""
        collector = collector_factory(books=BOOKS_GENRE)

        assert collector.get_books_with_specific_genre(GENRE_UNKNOWN) == []

    @pytest.mark.parametrize('genre', [GENRE_HORROR, GENRE_UNKNOWN])
    def test_get_books_with_specific_genre_empty_books_genre_correct_genre_empty_list(self, genre, collector_factory):
        """Любой жанр возвращает пустой список из пустой коллекции"""
        collector = collector_factory()

        assert collector.get_books_with_specific_genre(genre) == []

# ===== get_books_for_children ====================================================================================

    def test_get_books_for_children_correct_kids_book_success(self, collector_factory):
        """Детские книги"""
        collector = collector_factory(books=BOOKS_GENRE)

        books_for_children = collector.get_books_for_children()

        assert all(collector.books_genre.get(book) not in collector.genre_age_rating for book in books_for_children)

# ===== add_book_in_favorites =====================================================================================

    @pytest.mark.parametrize('add_tries_count', [1, 2, 3])
    def test_add_book_in_favorites_correct_named_book_several_times_favorites_len_one(self, add_tries_count, collector_factory):
        """Добавление в избранное без дубликатов"""
        collector = collector_factory(books=BOOKS_GENRE)

        for i in range(add_tries_count):
            collector.add_book_in_favorites(BOOK_HORROR)

        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_unknown_book_empty_favorites(self, collector_factory):
        """Добавление несуществующей книги в избранное"""
        collector = collector_factory(books=BOOKS_GENRE)

        collector.add_book_in_favorites(BOOK_UNKNOWN)

        assert len(collector.favorites) == 0

# ===== delete_book_from_favorites ================================================================================

    def test_delete_book_from_favorites_book_favorites_len_decreased_by_one(self, collector_factory):
        """Удаление из избранного"""
        collector = collector_factory(books=BOOKS_GENRE, favorites=[BOOK_HORROR])

        len_before = len(collector.favorites)

        collector.delete_book_from_favorites(BOOK_HORROR)
        
        assert len(collector.favorites) == len_before - 1

    def test_delete_book_from_favorites_unknown_book_favorites_len_not_changed(self, collector_factory):
        """Удаление неизвестной книги из избранного"""
        collector = collector_factory(books=BOOKS_GENRE, favorites=[BOOK_HORROR])
        
        len_before = len(collector.favorites)

        collector.delete_book_from_favorites(BOOK_UNKNOWN)
        
        assert len(collector.favorites) == len_before

# ===== get_list_of_favorites_books ===============================================================================

    def test_get_list_of_favorites_books_book_list_equal(self, collector_factory):
        """Получение списка избранного"""
        collector = collector_factory(books=BOOKS_GENRE)

        list_of_favorites_books = collector.get_list_of_favorites_books()

        assert set(list_of_favorites_books) == set(collector.favorites)
