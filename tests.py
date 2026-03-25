import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_init_correct_genere_list(self, book):
        assert book.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        
    def test_add_new_book_success(self, book):
        book.add_new_book('Дюна')
        assert 'Дюна' in book.books_genre
        assert book.books_genre['Дюна'] == ''
        
    @pytest.mark.parametrize("book_name, genre", [
        ("Дюна", "Фантастика"),
        ("Шерлок Холмс", "Детективы")
        ])
    def test_set_book_genre(self, book, book_name, genre):
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)
        assert book_name.books_genre[book_name] == genre

    def test_get_book_genre(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Фантастика')
        assert book.get_book_genre('Дюна') == 'Фантастика'
        
    def test_get_books_with_specific_genre(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Фантастика')
        result = book.get_books_with_specific_genre('Фантастика')
        assert len(result) == 1

    def test_get_books_genre(self, book):
        book.add_new_book('Дюна')
        book.set_book_genre('Дюна', 'Фантастика')
        assert book.books_genre == {'Дюна': 'Фантастика'}

    @pytest.mark.parametrize("book_name, genre", [
        ("Дюна", "Фантастика"),
        ("Шерлок Холмс", "Детективы")
        ])
    def test_get_books_for_children(self, book, book_name, genre):
        book.add_new_book(book_name)
        book.set_book_genre(book_name, genre)
        assert 'Дюна' in book.get_books_for_children

    def test_add_book_in_favorites(self, book):
        book.add_new_book('Дюна')
        book.add_book_in_favorites('Дюна')
        assert 'Дюна' in book.favorites

    def test_delete_book_from_favorites(self, book):
        book.add_new_book('Дюна')
        book.add_book_in_favorites('Дюна')
        book.delete_book_from_favorites('Дюна')
        assert 'Дюна' not in book.favorites
    
    def test_get_list_of_favorites_books(self, book):
        assert book.favorites == []
