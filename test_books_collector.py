import pytest
from main import BooksCollector


class TestBooksCollector:

    # add_new_book

    @pytest.mark.parametrize('book_name', ['', 'А' * 41])
    def test_add_new_book_with_invalid_length_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('book_name', ['A', 'A' * 40])
    def test_add_new_book_with_valid_length_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_added_book_has_empty_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # set_book_genre

    def test_set_book_genre_sets_genre_for_existing_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_set_book_genre_does_not_set_invalid_genre(self, collector):
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Роман')
        assert collector.get_book_genre('Что делать, если ваш кот хочет вас убить') == ''

    # get_books_with_specific_genre

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Dune')
        collector.add_new_book('It')
        collector.set_book_genre('Dune', 'Фантастика')
        collector.set_book_genre('It', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Dune']

    # get_books_for_children

    def test_get_books_for_children_returns_only_children_books(self, collector):
        collector.add_new_book('Волшебник Изумрудного города')
        collector.add_new_book('It')
        collector.set_book_genre('Волшебник Изумрудного города', 'Фантастика')
        collector.set_book_genre('It', 'Ужасы')

        assert collector.get_books_for_children() == ['Волшебник Изумрудного города']

    # favorites

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Dune')
        collector.add_book_in_favorites('Dune')

        assert collector.get_list_of_favorites_books() == ['Dune']
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Dune')
        collector.add_book_in_favorites('Dune')
        collector.delete_book_from_favorites('Dune')

        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_not_added_if_book_not_exists(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')

        assert collector.get_list_of_favorites_books() == []
