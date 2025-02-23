class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.borrow_book()
                return book
        return None

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.available:
                book.return_book()
                return book
        return None


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        book = library.borrow_book(isbn)
        if book:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book not available.")

    def return_book(self, library, isbn):
        for book in self.borrowed_books:
            if book.isbn == isbn:
                library.return_book(isbn)
                self.borrowed_books.remove(book)
                print(f"{self.name} returned {book.title}")
                return
        print("You don't have this book.")

    def view_borrowed_books(self):
        if not self.borrowed_books:
            print("No books borrowed.")
        for book in self.borrowed_books:
            print(book)


library = Library()
library.add_book(Book("1984", "George Orwell", "123456789"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "987654321"))

user = User("Alice")
library.display_books()
user.borrow_book(library, "123456789")
user.view_borrowed_books()
library.display_books()
user.return_book(library, "123456789")
library.display_books()
