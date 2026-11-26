import random

import pytest

from data_books_collector import *


class TestBooksCollector:

    def test_add_new_book_valid_name_book_added(self, books_collector):
        books_collector.add_new_book(data_book_name)

        assert len(books_collector.books_genre) == 1
    

    @pytest.mark.parametrize('book_lenght', [0, 41, 1000])
    def test_add_new_book_incorrect_name_book_not_added(self, books_collector, book_lenght):
        book = self.generate_name_book(book_lenght)
        books_collector.add_new_book(book)

        assert len(books_collector.books_genre) == 0

    def test_set_book_genre_correct_book_name_and_genre_set(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.set_book_genre(data_book_name, data_genre)

        assert books_collector.books_genre[data_book_name] == 'Детективы'

    def test_set_book_genre_correct_book_name_incorrect_genre_not_set(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.set_book_genre(data_book_name, 'один два три четыре')

        assert books_collector.books_genre[data_book_name] == ''


    def test_get_book_genre_book_with_genre_return_genre(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.set_book_genre(data_book_name, data_genre)

        assert books_collector.get_book_genre(data_book_name) == data_genre

    def test_set_book_genre_not_exist_name_correct_genre_not_set(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.set_book_genre('ааааааааа', data_genre)

        assert books_collector.books_genre[data_book_name] != data_genre

    def test_get_book_genre_not_exist_genre_return_none(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.set_book_genre(data_book_name, data_genre)

        assert books_collector.get_book_genre('ссссссссс') is None

    def test_get_book_genre_book_without_genre_return_empty_string(self, books_collector):
        books_collector.add_new_book(data_book_name)

        assert books_collector.get_book_genre(data_book_name) == ''

    def test_get_books_with_specific_genre_book_with_genre_return_list_with_one_book(self, books_collector):
        for book, genre in data_dict_book_and_genre.items():
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)

        assert books_collector.get_books_with_specific_genre('Комедии') == ['Третья книга']

    def test_get_books_with_specific_genre_empty_books_genre_return_empty_list(self, books_collector):
        assert books_collector.get_books_with_specific_genre('Комедии') == []

    def test_get_books_with_specific_genre_incorrect_genre_return_empty_list(self, books_collector):
        for book, genre in data_dict_book_and_genre.items():
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)

        assert books_collector.get_books_with_specific_genre('Три') == []

    def test_get_books_genre_one_book_return_list(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.set_book_genre(data_book_name, data_genre)

        assert books_collector.get_books_genre() == {data_book_name: data_genre}

    def test_get_books_for_children_book_for_children_return_list_one_book(self, books_collector):
        for book, genre in data_dict_book_and_genre_for_children.items():
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)

        assert books_collector.get_books_for_children() == ['Первая книга']

    @pytest.mark.parametrize('dict_books', [data_dict_book_and_genre_not_for_children, {}])
    def test_get_books_for_children_books_not_for_children_return_empty_list(self, books_collector, dict_books):
        for book, genre in dict_books.items():
            books_collector.add_new_book(book)
            books_collector.set_book_genre(book, genre)

        assert books_collector.get_books_for_children() == []

    def test_add_book_in_favorites_one_book_add(self, books_collector):
        books_collector.add_new_book(data_book_name)
        books_collector.add_book_in_favorites(data_book_name)

        assert books_collector.favorites == [data_book_name]

    def test_add_book_in_favorites_empty_books_genre_not_added(self, books_collector):
        books_collector.add_book_in_favorites(self.generate_name_book(10))

        assert len(books_collector.favorites) == 0

    def test_add_book_in_favorites_dublicate_favorite_not_added(self, books_collector):
        book = self.generate_name_book(10)
        books_collector.add_new_book(book)
        books_collector.add_book_in_favorites(book)
        books_collector.add_book_in_favorites(book)

        assert books_collector.favorites == [book]

    def test_delete_book_from_favorites_one_book_deleted(self, books_collector):        
        books_collector.add_new_book(data_book_name)
        books_collector.add_book_in_favorites(data_book_name)
    
        books_collector.delete_book_from_favorites(data_book_name)

        assert books_collector.favorites == []

    def test_delete_book_from_favorites_delete_not_axist_book_not_deleted(self, books_collector):
        list_book = self.generate_list_book(3)
        for i in range(len(list_book) - 1):
            books_collector.add_new_book(list_book[i])
            books_collector.add_book_in_favorites(list_book[i])
        books_collector.delete_book_from_favorites(list_book[2])

        assert books_collector.favorites == list_book[0:2]

    def test_get_list_of_favorites_books_correct_book_added(self, books_collector):
        book = self.generate_name_book(10)
        books_collector.add_new_book(book)
        books_collector.add_book_in_favorites(book)

        assert books_collector.get_list_of_favorites_books() == [book]

    def test_get_list_of_favorites_empty_favorites_return_empty_list(self, books_collector):
        assert books_collector.get_list_of_favorites_books() == []

    def generate_list_book(self, number):
        result = []

        while len(result) < number:
            s = self.generate_name_book(10)
            if s not in result:
                result.append(s)

        return result

    def generate_name_book(self, lenght):
        string_for_generate_name = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        return ''.join(random.choices(string_for_generate_name, k=lenght))
