import pytest
from main import BooksCollector

class TestBooksCollector():
    def test_add_new_book_add_books_without_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_books_wit_name_large_41_char(self):
        collector = BooksCollector()
        collector.add_new_book('Жизнь, необыкновенные и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего двадцать восемь лет в полном одиночестве на необитаемом острове у берегов Америки близ устьев реки Ориноко, куда он был выброшен кораблекрушением, во время которого весь экипаж корабля, кроме него, погиб; с изложением его неожиданного освобождения пиратами. Написано им самим')
        assert len(collector.books_genre) == 0

    def test_set_book_genre_set_allowed_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Долгая прогулка')
        collector.set_book_genre('Долгая прогулка', 'Ужасы')
        assert list(collector.books_genre.values()) == ['Ужасы']

    def test_set_book_genre_set_not_allowed_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга с неправильным жанром')
        collector.set_book_genre('Книга с неправильным жанром', 'Неправильный жанр')
        assert '' in collector.books_genre.values()

    @pytest.mark.parametrize(
        'book_name, genre_name',
        [
            ['Автостопом по галактике', 'Фантастика'],
            ['Долгая прогулка', 'Ужасы'],
        ]
    )
    def test_get_book_genre_get_recorded_genre_behind_book(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_book_genre(book_name) == genre_name

    def test_get_books_with_specific_genre_get_list_right_books(self):
        collector = BooksCollector()
        collector.add_new_book('Долгая прогулка')
        collector.set_book_genre('Долгая прогулка', 'Ужасы')
        collector.add_new_book('Падение дома Ашеров')
        collector.set_book_genre('Падение дома Ашеров', 'Ужасы')
        collector.add_new_book('Похождения бравого солдата Швейка')
        collector.set_book_genre('Похождения бравого солдата Швейка', 'Комедии')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Долгая прогулка', 'Падение дома Ашеров']

    def test_get_books_genre_get_full_collection(self):
        collector = BooksCollector()
        collector.add_new_book('Падение дома Ашеров')
        collector.set_book_genre('Падение дома Ашеров', 'Ужасы')
        collector.add_new_book('Похождения бравого солдата Швейка')
        collector.set_book_genre('Похождения бравого солдата Швейка', 'Комедии')
        assert collector.get_books_genre() == {'Падение дома Ашеров': 'Ужасы', 'Похождения бравого солдата Швейка': 'Комедии'}

    @pytest.mark.parametrize(
        'book_name, genre_name',
        [
            ['Автостопом по галактике', 'Фантастика'],
            ['Долгая прогулка', 'Ужасы'],
            ['Падение дома Ашеров', 'Детективы'],
            ['Бэтмен. Убийственная шутка', 'Мультфильмы'],
            ['Похождения бравого солдата Швейка', 'Комедии']
        ]
    )
    def test_get_books_for_children_get_books_only_for_children(self, book_name, genre_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre_name)
        assert collector.get_books_for_children() not in collector.genre_age_rating

    def test_add_book_in_favorites_add_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Падение дома Ашеров')
        collector.add_book_in_favorites('Падение дома Ашеров')
        assert list(collector.favorites)[0] == 'Падение дома Ашеров'

    def test_add_book_in_favorites_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Падение дома Ашеров')
        collector.add_book_in_favorites('Падение дома Ашеров')
        collector.add_book_in_favorites('Падение дома Ашеров')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_delete_1_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Падение дома Ашеров')
        collector.add_book_in_favorites('Падение дома Ашеров')
        collector.delete_book_from_favorites('Падение дома Ашеров')
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_adding_2_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Падение дома Ашеров')
        collector.add_book_in_favorites('Падение дома Ашеров')
        collector.add_new_book('Автостопом по галактике')
        collector.add_book_in_favorites('Автостопом по галактике')
        assert collector.get_list_of_favorites_books() == ['Падение дома Ашеров', 'Автостопом по галактике']
