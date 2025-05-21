# Sprint_4

## Тесты для класса BooksCollector

### Метод `add_new_book`
1. **test_add_new_book_correct_book_true**  
   _Книга с корректным названием добавляется в список._  
   Проверяет, что книга появляется в словаре `books_genre`.

2. **test_add_new_book_correct_book_empty_genre**  
   _Книга с корректным названием добавляется в список._  
   Убеждается, что жанр по умолчанию — пустая строка.

3. **test_add_new_book_correct_named_two_books_len_one**  
   _Две одинаковые книги корректной длины — добавляется только одна._  
   Проверяет уникальность книг в коллекции.

4. **test_add_new_book_incorrect_named_book_len_zero**  
   _Книги с некорректным названием не добавляются._  
   Тестирует обработку пустых строк и названий длиннее 40 символов.

---

### Метод `get_books_genre`
5. **test_get_books_genre_correct_named_book_genre_dict_equal**  
   _Полученный словарь книга-жанр идентичен по значениям инициализированному._  
   Сравнивает возвращаемый словарь с исходным.

---

### Метод `get_book_genre`
6. **test_get_book_genre_correct_book_genre_true**  
   _Полученный жанр книги совпадает с инициализированным._  
   Проверяет корректность возвращаемого жанра для существующей книги.

---

### Метод `set_book_genre`
7. **test_set_book_genre_correct_book_genre_true**  
   _Жанр книги устанавливается корректно, если книга есть в коллекции._  
   Проверяет обновление жанра для добавленной книги.

---

### Метод `get_books_with_specific_genre`
8. **test_get_books_with_specific_genre_correct_named_book_genre_dict_correct_genre_equal**  
   _Проверка получения книг определенного жанра со списком корректных жанров._  
   Убеждается, что возвращаются только книги с указанным жанром.

9. **test_get_books_with_specific_genre_correct_named_book_genre_dict_incorrect_genre_empty_list**  
   _Проверка получения книг определенного жанра со списком некорректных жанров._  
   Возвращает пустой список для несуществующего жанра.

10. **test_get_books_with_specific_genre_empty_books_genre_correct_genre_empty_list**  
    _Проверка получения книг определенного жанра с пустым словарем._  
    Тестирует обработку пустой коллекции.

---

### Метод `get_books_for_children`
11. **test_get_books_for_children_correct_kids_book_equal**  
    _Проверка получения книг детского рейтинга со списком взрослых жанров._  
    Исключает книги с жанрами из `genre_age_rating`.

---

### Метод `add_book_in_favorites`
12. **test_add_book_in_favorites_correct_named_one_book_favorites_len_one**  
    _Проверка добавления книги в избранное, если книга уже есть в коллекции._  
    Убеждается, что книга появляется в списке `favorites`.

13. **test_add_book_in_favorites_correct_named_two_same_book_favorites_len_one**  
    _Проверка добавления двух одинаковых книг в избранное._  
    Игнорирует дубликаты в избранном.

14. **test_add_book_in_favorites_one_book_not_in_collector_empty_favorites**  
    _Проверка добавления в избранное книги, которой нет в коллекции._  
    Блокирует добавление несуществующих книг.

---

### Метод `delete_book_from_favorites`
15. **test_delete_book_from_favorites_exists_book_empty_favorites**  
    _Удаление из избранного книги, которая там есть._  
    Проверяет корректное удаление существующей книги.

16. **test_delete_book_from_favorites_not_exists_book_favorites_lists_not_changed**  
    _Удаление из избранного книги, которой там нет._  
    Гарантирует, что список не меняется при удалении отсутствующей книги.

---

### Метод `get_list_of_favorites_books`
17. **test_get_list_of_favorites_books_book_list_equal**  
    _Получение списка избранного и сравнение с инициализируемым._  
    Проверяет, что возвращаемый список соответствует ожидаемому.