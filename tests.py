import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_init_correct_genre_list(self, book):
        assert book.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_add_new_book_success(self, book):
        book.add_new_book('Дюна')
        assert 'Дюна' in book.books_genre
        assert book.books_genre['Дюна'] == ''

    def test_add_new_book_twice(self, book):
        book.add_new_book('Дюна')
        book.add_new_book('Дюна')
        assert 'Дюна' in book.books_genre
        assert len(book.books_genre) == 1

    def test_add_new_book_len_0(self, book):
        book.add_new_book('')
        assert '' not in book.books_genre

    def test_add_new_book_len_41(self, book):
        st_41 = 'A'*41
        book.add_new_book(st_41)
        assert st_41 not in book.books_genre

    @pytest.mark.parametrize('book_name, genre', [
        ('Дюна', 'Фантастика'),
        ('Шерлок Холмс', 'Детективы')
        ])
    def test_set_book_genre(self, book, book_name, genre):
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)
        assert book.books_genre[book_name] == genre

    def test_set_book_genre_if_name_not_in_books_genre(self, book):
        book.set_book_genre('Дюна', 'Фантастика')
        assert len(book.books_genre) == 0

    def test_set_book_genre_if_genre_not_in_genere_list(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Несуществующий')
        assert book.books_genre['Дюна'] == ''

    def test_get_book_genre(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Фантастика')
        assert book.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre(self, book):
        book.add_new_book('Дюна')
        book.add_new_book('Шерлок Холмс')
        book.set_book_genre('Дюна', 'Фантастика')
        book.set_book_genre('Шерлок Холмс', 'Детективы')
        result = book.get_books_with_specific_genre('Фантастика')
        assert  result == ['Дюна']

    def test_get_books_genre(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Фантастика')
        assert book.books_genre == {'Дюна': 'Фантастика'}

    def test_get_books_for_children(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Фантастика')
        assert 'Дюна' in book.get_books_for_children()

    def test_get_books_for_children_book_with_age_rating(self, book):
        book.add_new_book('Шерлок Холмс')
        book.set_book_genre('Шерлок Холмс', 'Детектив')
        assert 'Шерлок Холмс' not in book.get_books_for_children()

    def test_add_book_in_favorites(self, book):
        book.add_new_book('Дюна')
        book.add_book_in_favorites('Дюна')
        assert 'Дюна' in book.favorites

    def test_add_book_in_favorites_twice(self, book):
        book.add_new_book('Дюна')
        book.add_book_in_favorites('Дюна')
        book.add_book_in_favorites('Дюна')
        assert len(book.favorites) == 1
        
    def test_delete_book_from_favorites(self, book):
        book.add_new_book('Дюна')
        book.add_book_in_favorites('Дюна')
        book.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in book.favorites

    def test_get_list_of_favorites_books(self, book):
        book.add_new_book('Дюна')
        book.add_book_in_favorites('Дюна')
        assert book.get_list_of_favorites_books() == ['Дюна']  

