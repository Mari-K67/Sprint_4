# Sprint_4
Unit testing.

Task: cover the `BooksCollector` application with tests. It allows you to set the genre of books and add them to favorites.  
The `BooksCollector` class contains:
* Dictionary `books_genre`, where you can add a pair `Book title: Book genre`.
* List `favorites`, which contains favorite books.
* List `genre`, which contains available genres.
* List `genre_age_rating`, which contains genres with age ratings.
* A set of methods for working with the `books_genre` dictionary and `favorites` list: 
  * `add_new_book` — adds a new book to the dictionary without specifying a genre. The book title can contain a maximum of 40 characters. You can add the same book only once.
  * `set_book_genre` — sets the genre of a book if the book is in `books_genre` and its genre is in the `genre` list.
  * `get_book_genre` — returns the genre of a book by its name.
  * `get_books_with_specific_genre` — returns a list of books with a specific genre.
  * `get_books_genre` — returns the current `books_genre` dictionary.
  * `get_books_for_children` — returns books that are suitable for children. The book's genre should not have an age rating.
  * `add_book_in_favorites` — adds a book to favorites. The book must be in the `books_genre` dictionary. You cannot add a book to favorites again.
  * `delete_book_from_favorites` — removes a book from favorites if it is there.
  * `get_list_of_favorites_books` — gets a list of favorite books.

```
class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']
    
    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр 
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites
```
