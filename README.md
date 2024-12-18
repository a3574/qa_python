# qa_python
# def test_add_new_book_add_two_books - ранее написанный тест, добавил в main метод get_books_rating() чтобы тест работал. Возможно нужено было заменить в непосредственно в тесте метод на get_book_genre, но я непонял.

# Тесты для проверки метода add_new_book:
# test_add_new_book_add_books_without_name - Тест на проверку вставки названия книги без названия
# test_add_new_book_add_books_wit_name_large_41_char - Тест на проверку вставки названия книги больше верхней границы разрешенного - 41 символов

# Тесты для проверки метода set_book_genre:
# test_set_book_genre_set_allowed_book_genre - Тест на проверку добавления книги по каждому из разрешенных жанров
# test_set_book_genre_set_not_allowed_book_genre - Тест на проверку добавления книги с неправильным жанром

# Тесты для проверки метода get_book_genre:
# test_get_book_genre_get_recorded_genre_behind_book - Тест на проверку получения книги по указанному жанру

# Тесты для проверки метода get_books_with_specific_genre:
# test_get_books_with_specific_genre_get_list_right_books - Тест на проверку возврата соответствующего книги жанра

# Тесты для проверки метода get_books_genre:
# test_get_books_genre_get_full_collection - Тест на возврат всех книг добавленных в коллекцию

# Тесты для проверки метода get_books_for_children:
# test_get_books_for_children_get_books_only_for_children - Тест на проверку того что полученные через get_books_for_children книги не попадают в genre_age_rating 

# Тесты для проверки метода add_book_in_favorites:
# test_add_book_in_favorites_add_book_not_in_favorites -- Проверка на штатное добавление книги в favorites, т.е. книги, которая еще не там.
# test_add_book_in_favorites_add_book_in_favorites -- Проверка на повтороное добавление книги в favorites, т.е. книги, которая уже там.

# Тесты для проверки метода delete_book_from_favorites:
# test_delete_book_from_favorites_delete_1_book_from_favorites Проверка на штатное удаление книги из favorites.

# Тесты для проверки метода get_list_of_favorites_books:
# test_get_list_of_favorites_books_adding_2_books_in_favorites -- Проверка метода на вывод пары книг добавленных в favorites