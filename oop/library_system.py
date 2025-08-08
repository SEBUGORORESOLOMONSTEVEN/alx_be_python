#!/usr/bin/env python3
"""
library_system.py

This script defines a system of classes for a library, showcasing
inheritance and composition. It includes a base Book class, derived
EBook and PrintBook classes, and a Library class to manage them.
"""

class Book:
    """
    A base class to represent a generic book.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance with a title and an author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book's title and author.
        """
        return f"{self.title} by {self.author}"


class EBook(Book):
    """
    A derived class for electronic books (e-books), inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance, calling the base class constructor
        and adding a unique attribute for file size.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation that includes the file size.
        """
        return f"{super().__str__()}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A derived class for physical books, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance, calling the base class constructor
        and adding a unique attribute for page count.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation that includes the page count.
        """
        return f"{super().__str__()}, Page Count: {self.page_count}"


class Library:
    """
    A class that demonstrates composition by managing a collection of books.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list to store books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.
        This method demonstrates composition, as a Library is "composed of" Book objects.
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints the details of each book currently in the library,
        demonstrating polymorphism and checking the object's type.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book}")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book}")
            else:
                print(f"Book: {book}")


