import unittest
from library_system import Book, add_book, InvalidISBNException

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = {}

    def test_add_valid_book(self):
        # This test covers the case where the ISBN is valid
        book = Book("Sample Book", "Author Name", "1234567890123")
        add_book(self.library, book)
        self.assertIn("1234567890123", self.library)
        self.assertEqual(self.library["1234567890123"], book)

    def test_add_book_invalid_isbn_not_string(self):
        # This test covers the condition where the ISBN is not a string
        book = Book("Sample Book", "Author Name", 1234567890123)
        with self.assertRaises(InvalidISBNException):
            add_book(self.library, book)

    def test_add_book_invalid_isbn_length_short(self):
        # This test covers the condition where the ISBN is shorter than 13 characters
        book = Book("Sample Book", "Author Name", "123456789012")
        with self.assertRaises(InvalidISBNException):
            add_book(self.library, book)

    def test_add_book_invalid_isbn_length_long(self):
        # This test covers the condition where the ISBN is longer than 13 characters
        book = Book("Sample Book", "Author Name", "12345678901234")
        with self.assertRaises(InvalidISBNException):
            add_book(self.library, book)

    def test_add_book_invalid_isbn_non_digit(self):
        # This test covers the condition where the ISBN contains non-digit characters
        book = Book("Sample Book", "Author Name", "ABCDEFGHIJKLM")
        with self.assertRaises(InvalidISBNException):
            add_book(self.library, book)

if __name__ == "__main__":
    unittest.main()
