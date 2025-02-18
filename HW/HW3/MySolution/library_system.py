class InvalidISBNException(Exception):
    """Exception raised for errors in the input ISBN."""

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

def add_book(library, book):
    """
    Adds a book to the library dictionary if the ISBN is valid.
    
    Args:
    library (dict): The dictionary to store books, keyed by ISBN.
    book (Book): The book object to add.

    Raises:
    InvalidISBNException: If the ISBN does not meet the required conditions.
    """
    # Check if the ISBN is a string, is 13 characters long, and contains only digits.
    if not isinstance(book.isbn, str) or len(book.isbn) != 13 or not book.isbn.isdigit():
        print(f"Invalid ISBN: {book.isbn}") 
        raise InvalidISBNException(f"Invalid ISBN: {book.isbn}")
    
    # Add the book to the library if the ISBN is valid.
    library[book.isbn] = book
